from pathlib import Path
import pytest

from memestra import memestra, nbmemestra
# from nbmemestra import nbmemestra
from pyls_memestra.plugin import format_text
from pyls.workspace import Document

here = Path(__file__).parent

def test_pyls_file():
    path = here / "file.py"
    with open(path, 'r') as code:
        deprecated_uses = memestra(code, decorator=("decorator", "deprecated"))
        assert deprecated_uses == [('foo',
            '/home/mariana/Development/pyls-memestra/tests/file.py',
            7, 4),
            ('foo',
            '/home/mariana/Development/pyls-memestra/tests/file.py',
            9, 0)]

def test_pyls_format_text_syntax():
    keywords = [('foo', '', 7, 4), ('foo', '', 9, 0)]

    result = format_text(keywords, [])
    assert result == [
   {
      "source":"memestra",
      "range":{
         "start":{
            "line":6,
            "character":4
         },
         "end":{
            "line":6,
            "character":3
         }
      },
      "message":"foo is deprecated.",
      "severity":3
   },
   {
      "source":"memestra",
      "range":{
         "start":{
            "line":8,
            "character":0
         },
         "end":{
            "line":8,
            "character":3
         }
      },
      "message":"foo is deprecated.",
      "severity":3
   }
]
