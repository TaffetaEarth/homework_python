def show(func):
    def new_func(*args, **kwargs):
        print('Name of function', func.__name__)
        print("Positional args", args)
        print("Keywords:", kwargs)
        res = func(*args, **kwargs)
        print("Result: ", res)
        return res
    return new_func


@show
def sum(a, b):
    return a+b


sum(1, b=3)
