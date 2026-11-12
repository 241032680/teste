foo_called, bar_called = False, False

def example(foo=False, bar=False):
    global foo_called, bar_called
    foo_called = 1*foo
    bar_called = 1*bar
    return foo_called, bar_called

def check():
    if foo_called:
       print("foo called")
       if not bar_called: print("---------")
    if bar_called:
        print("bar called")
        if not foo_called: print("---------")
    if not bool(foo_called) ^ bool(bar_called):
        print("-------")

example("foo")
check()

example(bar="bar")
check()

example("foo", "bar")
check()
