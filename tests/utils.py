
def setup (f):
    def wrapper (self, *args, **kwargs):
        self.setUp()
        return f(self, *args, **kwargs)
    wrapper.__name__ = f.__name__
    wrapper.__qualname__ = f.__qualname__
    return wrapper

class TestCase:
    def setUp (self):
        pass
