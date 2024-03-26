from time import perf_counter
from functools import wraps


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args):
        start_time = perf_counter()
        result = func(*args)
        end_time = perf_counter()
        total_time = end_time - start_time

        if args:
            print(f'Function {func.__name__} - data.{len(args[0])}, Took {total_time:.4f} seconds')
        else:
            print(f'Function {func.__name__}, Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper
