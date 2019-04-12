import functools
import time


def test(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("first")
        func(*args, **kwargs)
        print("second")
        return func(*args, **kwargs)
    return wrapper


def timer(func):
    functools.wraps(func)

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = start_time-end_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")

#         return value
#     return wrapper
# def dec(func):
#     def wrapper(n):
#         print (n)
#         res=foo(n)+"hell"
#         return res
# def foo(name):
#     return name

# @dec
# foo("mahmoud")
