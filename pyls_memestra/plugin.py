import os
from pylsp import hookimpl, lsp
from memestra import memestra

import logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# TODO: use lsp.DiagnosticTag once https://github.com/python-lsp/python-lsp-server/pull/142 is merged
class DiagnosticTag:
    Unnecessary = 1
    Deprecated = 2

@hookimpl
def pylsp_settings():
    return {
        "plugins": {
            "pyls-memestra": {
                "enabled": True,
                "recursive": False,
                "decorator_module": "deprecated",
                "decorator_function": "deprecated",
                "reason_keyword": "reason",
                "cache_dir": None,
                "additional_search_paths": []
            }
        }
    }

@hookimpl
def pylsp_lint(config, document):
    # print("pyls_lint 🐔")
    settings = config.plugin_settings('pyls-memestra',
                                      document_path=document.path)
    diagnostics = []
    search_paths = [os.path.dirname(os.path.abspath(document.path))]
    search_paths.extend(settings.get('additional_search_paths'))
    supported_tags = set(
        config.capabilities
        .get('textDocument', {})
        .get('publishDiagnostics', {})
        .get('tagSupport', {})
        .get('valueSet', set())
    )

    try:
        with open(document.path, 'r', encoding="utf-8") as code:
            deprecated_uses = memestra(
                code,
                decorator=(settings.get('decorator_module'),
                           settings.get('decorator_function')),
                reason_keyword=settings.get('reason_keyword'),
                recursive=settings.get('recursive'),
                cache_dir=settings.get('cache_dir'),
                search_paths=search_paths)
            diagnostics = format_text(deprecated_uses, diagnostics, supported_tags)
    except SyntaxError as e:
        logger.error('Syntax error at {} - {} ({})', e.line, e.column, e.message)
        raise e
    return diagnostics

def format_text(deprecated_uses, diagnostics, supported_tags=None):
    if supported_tags is None:
        supported_tags = set()
    tags = [DiagnosticTag.Deprecated]
    for fname, fd, lineno, colno, reason in deprecated_uses:
        err_range = {
            'start': {'line': lineno - 1, 'character': colno},
            'end': {'line': lineno - 1, 'character': colno + len(fname)},
        }
        if reason and reason != "reason":
            message = fname + " is deprecated. " + reason
        else:
            message = fname + " is deprecated."

        diagnostic = {
            'source': 'memestra',
            'range': err_range,
            'message': message,
            'severity': lsp.DiagnosticSeverity.Information,
        }

        if DiagnosticTag.Deprecated in supported_tags:
            diagnostic['tags'] = tags
        diagnostics.append(diagnostic)
    return diagnostics
