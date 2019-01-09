import inspect


def decorator(argument):
    def real_decorator(function):
        def wrapper(v):
            # funny_stuff()
            x = v + argument
            # something_with_argument(argument)
            result = function(x)
            function.tag = "nnn"
            # more_funny_stuff()
            return result

        return wrapper

    return real_decorator


class B:
    pass


class T:
    def __init__(self):
        self.f = '123'


class A(B):
    def __init__(self, c=None):
        self.a = None
        self._b = None
        self.c = c
        self.t = T()


    def b(self):
        return self._b

    def set_b(self, b):
        self._b = b

    b = property(b, set_b)


a = A()
print(a.attr.temp)

# print(type(a))
# a2 = type(a)(9)

# print(a2.c)
# print(isinstance(a, B))


def isprop(v):
    return isinstance(v, property)


'''
for i in a.__dict__:
    if i == 't':
        print(a.__dict__[i].f)
    print(i)
'''
propnames = [(name, value) for (name, value) in inspect.getmembers(A, isprop)]
# a.__[propnames[0]] = 10
# a.__getitem__[propnames[0]] = 10
print(propnames[0])

print()
