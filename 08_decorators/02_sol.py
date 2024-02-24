
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        # kwargs_value = ', '.join('%s=%s' % (key, value) for key, value in sorted(kwargs.items()))
        kwargs_value = ', '.join(f"{key} : {value}" for key, value in kwargs.items())
        print(f'Calling function :{func.__name__} with args: {args_value} ; and kwargs: {kwargs_value}')
        return func(*args, **kwargs)

    return wrapper

@debug
def hello():
    print("Hello")

hello()

@debug
def greet(name, greeting = "Hello Ji"):
    print(f"{greeting}, {name}!")

greet("chai", greeting = "Haan Ji")
