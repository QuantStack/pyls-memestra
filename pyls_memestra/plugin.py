# Copyright 2017 Palantir Technologies, Inc.
from pyls import hookimpl, lsp
from memestra import memestra

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@hookimpl
def pyls_lint(document):
    diagnostics = []
    with open(document.path, 'r') as code:
        deprecate_uses = memestra(code, decorator=("decorator", "deprecated"))
        for fname, fd, lineno, colno in deprecate_uses:
            err_range = {
                'start': {'line': lineno - 1, 'character': colno},
                'end': {'line': lineno - 1, 'character': len(fname)},
            }
            severity = lsp.DiagnosticSeverity.Information
            diagnostics.append({
                'source': 'memestra',
                'range': err_range,
                'message': fname + " is deprecated.",
                'severity': lsp.DiagnosticSeverity.Information,
            })
    return diagnostics
