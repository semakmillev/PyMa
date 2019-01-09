from functools import partial

text_xml = '<client><name>Semak</name><passport num="4608229176"/></client>'


# def add(n):
#    return n + 1
def child_decorator(tag):
    def real_decorator(cls):
        def wrapper(v):
            # funny_stuff()
            #x = v + argument
            # something_with_argument(argument)
            #result = function(x)
            # more_funny_stuff()
            return result
        return wrapper

    return real_decorator




a = Client()


def decorator(argument):
    def real_decorator(function):
        def wrapper(v):
            # funny_stuff()
            x = v + argument
            # something_with_argument(argument)
            result = function(x)
            # more_funny_stuff()
            return result

        return wrapper

    return real_decorator


@decorator(10)
def test(v):
    print(v)


test(5)
