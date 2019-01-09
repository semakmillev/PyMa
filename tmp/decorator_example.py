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




@decorator(10)
def test(v):
    print(v)

test(5)


