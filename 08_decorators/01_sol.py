import time

def timer(func):
    def  wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in {abs(start_time - end_time)} time")
        return result

    return wrapper


@timer
def example_function(n):
    time.sleep(n)
    print(n)
    
example_function(2)

# timer(example_function(4))
