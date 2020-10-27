from pyls import hookimpl, lsp
from memestra import memestra

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@hookimpl
def pyls_lint(document):
    diagnostics = []
    with open(document.path, 'r') as code:
        deprecated_uses = memestra(code, decorator=("deprecated", "deprecated"),
            reason_keyword="reason")
        diagnostics = format_text(deprecated_uses, diagnostics)
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
