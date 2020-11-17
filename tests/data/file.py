import deprecated
from importtest import imported

@deprecated.deprecated('deprecated at some point')
def foo(): pass

def bar():
    foo()

imported()
