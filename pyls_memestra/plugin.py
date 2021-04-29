import os
from pylsp import hookimpl, lsp
from memestra import memestra

import logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

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
    print("pyls_lint 🐔")
    settings = config.plugin_settings('pyls-memestra',
                                      document_path=document.path)
    diagnostics = []
    search_paths = [os.path.dirname(os.path.abspath(document.path))]
    search_paths.extend(settings.get('additional_search_paths'))
    try:
        with open(document.path, 'r') as code:
            deprecated_uses = memestra(
                code,
                decorator=(settings.get('decorator_module'),
                           settings.get('decorator_function')),
                reason_keyword=settings.get('reason_keyword'),
                recursive=settings.get('recursive'),
                cache_dir=settings.get('cache_dir'),
                search_paths=search_paths)
            diagnostics = format_text(deprecated_uses, diagnostics)
    except SyntaxError as e:
        logger.error('Syntax error at {} - {} ({})', e.line, e.column, e.message)
        raise e
    return diagnostics

def format_text(deprecated_uses, diagnostics):
    for fname, fd, lineno, colno, reason in deprecated_uses:
        err_range = {
            'start': {'line': lineno - 1, 'character': colno},
            'end': {'line': lineno - 1, 'character': colno + len(fname)},
        }
        if reason and reason != "reason":
            diagnostics.append({
                'source': 'memestra',
                'range': err_range,
                'message': fname + " is deprecated. " + reason,
                'severity': lsp.DiagnosticSeverity.Information,
            })
        else:
            diagnostics.append({
                'source': 'memestra',
                'range': err_range,
                'message': fname + " is deprecated.",
                'severity': lsp.DiagnosticSeverity.Information,
            })
    return diagnostics
