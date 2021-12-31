import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import Mock
from copy import deepcopy
import pytest

from memestra import memestra, nbmemestra
from pyls_memestra.plugin import format_text, pylsp_lint, pylsp_settings
from pylsp import uris
from pylsp.config.config import Config
from pylsp.workspace import Workspace, Document

here = Path(__file__).parent
data = here / "data"

@pytest.fixture
def config(tmpdir):
    config = Config(uris.from_fs_path(str(tmpdir)), {}, 0, {})
    config.update(pylsp_settings())
    return config

@pytest.fixture
def workspace(tmpdir, config):
    ws = Workspace(uris.from_fs_path(str(tmpdir)), Mock())
    ws._config = config
    return ws

@pytest.yield_fixture
def document(workspace):
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)

    def write_doc(text):
        temp_file.write(text)
        temp_file.close()
        doc = Document(uris.from_fs_path(temp_file.name), workspace)
        return doc

    yield write_doc
    os.remove(temp_file.name)

def build_diagnostic(name, start, end, reason, source="memestra", severity=3, tags=None):
    if reason is None:
        message = name + " is deprecated."
    else:
        message = name + " is deprecated. " + reason

    diagnostic = {
            "source": source,
            "range": {
                "start": {
                    "line": start[0],
                    "character": start[1]
                },
                "end": {
                    "line": end[0],
                    "character": end[1]
                }
            },
            "message": message,
            "severity": severity,
        }
    if tags is not None:
        diagnostic["tags"] = tags
    return diagnostic

def update_setting(config, name, value):
    settings = deepcopy(config._settings)
    settings["plugins"]["pyls-memestra"][name] = value
    config.update(settings)

def test_basic(workspace, config):
    doc = Document(uris.from_fs_path(str(data / "file.py")), workspace)
    diagnostics = pylsp_lint(config, doc)

    assert diagnostics == [
        build_diagnostic("foo", (7, 4), (7, 7), "deprecated at some point"),
        build_diagnostic("imported", (9, 0), (9, 8), "test reason"),
    ]


def test_tag_support(workspace, config):
    doc = Document(uris.from_fs_path(str(data / "file.py")), workspace)
    config.capabilities['textDocument'] = {
        'publishDiagnostics': {'tagSupport': {'valueSet': [2]}}
    }
    diagnostics = pylsp_lint(config, doc)

    assert diagnostics == [
        build_diagnostic("foo", (7, 4), (7, 7), "deprecated at some point", tags=[2]),
        build_diagnostic("imported", (9, 0), (9, 8), "test reason", tags=[2]),
    ]

def test_tag_absent(workspace, config):
    doc = Document(uris.from_fs_path(str(data / "file.py")), workspace)
    config.capabilities['textDocument'] = {
        'publishDiagnostics': {'tagSupport': {'valueSet': [1]}}
    }
    diagnostics = pylsp_lint(config, doc)

    assert diagnostics == [
        build_diagnostic("foo", (7, 4), (7, 7), "deprecated at some point", tags=None),
        build_diagnostic("imported", (9, 0), (9, 8), "test reason", tags=None),
    ]

def test_decorator_name(workspace, config, document):
    doc = document("""
import bogus

@bogus.deprecateme("nope")
def foo():
    pass

foo()
""")
    update_setting(config, "decorator_module", "bogus")
    update_setting(config, "decorator_function", "deprecateme")
    diagnostics = pylsp_lint(config, doc)

    assert diagnostics == [
        build_diagnostic("foo", (7, 0), (7, 3), "nope"),
    ]

def test_reason_keyword(workspace, config, document):
    doc = document("""
import deprecated

@deprecated.deprecated(excuse="too old")
def foo():
    pass

foo()
""")
    update_setting(config, "reason_keyword", "excuse")
    diagnostics = pylsp_lint(config, doc)

    assert diagnostics == [
        build_diagnostic("foo", (7, 0), (7, 3), "too old"),
    ]

def test_empty_reason(workspace, config, document):
    doc = document("""
import deprecated

@deprecated.deprecated
def foo():
    pass

foo()
""")
    update_setting(config, "reason_keyword", "excuse")
    diagnostics = pylsp_lint(config, doc)

    assert diagnostics == [
        build_diagnostic("foo", (7, 0), (7, 3), None),
    ]

@pytest.mark.skip("This test needs improvements to memestra imports")
def test_recursive(workspace, config, document):
    doc = document("""
from testpackage import bar

bar()
""")
    update_setting(config, "recursive", True)
    diagnostics = pylsp_lint(config, doc)

    assert diagnostics == [
        build_diagnostic("bar", (3, 0), (3, 3), "nested"),
    ]

def test_search_paths(workspace, config, document):
    doc = document("""
from bar import bar

bar()
""")
    update_setting(config, "additional_search_paths",
                   [str(data / "testpackage")])
    diagnostics = pylsp_lint(config, doc)

    assert diagnostics == [
        build_diagnostic("bar", (3, 0), (3, 3), "nested"),
    ]

@pytest.mark.skipif(sys.platform == 'win32', reason='failing on windows')
def test_cache_dir(workspace, config, document):
    doc = document("""
from cachetest import bar

bar()
""")
    update_setting(config, "additional_search_paths", [str(data)])
    update_setting(config, "cache_dir", str(data / "cache"))
    diagnostics = pylsp_lint(config, doc)

    assert diagnostics == [
        build_diagnostic("bar", (3, 0), (3, 3), "cached"),
    ]

def test_pyls_format_text_syntax():
    keywords = [('foo', '', 7, 4, 'reason1'), ('foo', '', 9, 0, 'reason2')]

    result = format_text(keywords, [])
    assert result == [
        build_diagnostic("foo", (6, 4), (6, 7), 'reason1'),
        build_diagnostic("foo", (8, 0), (8, 3), 'reason2')
    ]
