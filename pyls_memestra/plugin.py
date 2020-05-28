from pyls import hookimpl, lsp
from memestra import memestra

@hookimpl
def pyls_lint(document):
    diagnostics = []
    with open(document.path, 'r') as code:
        deprecated_uses = memestra(code, decorator=("decoratortest", "deprecated"))
        diagnostics = format_text(deprecated_uses, diagnostics)
    return diagnostics

def format_text(deprecated_uses, diagnostics):
    for fname, fd, lineno, colno in deprecated_uses:
        err_range = {
            'start': {'line': lineno - 1, 'character': colno},
            'end': {'line': lineno - 1, 'character': len(fname)},
        }
        diagnostics.append({
            'source': 'memestra',
            'range': err_range,
            'message': fname + " is deprecated.",
            'severity': lsp.DiagnosticSeverity.Information,
        })
    return diagnostics
