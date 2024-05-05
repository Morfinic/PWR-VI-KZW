from time import perf_counter
from functools import wraps


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args):
        nonlocal total
        start_time = perf_counter()
        result = func(*args)
        end_time = perf_counter()
        exec_duration = end_time - start_time
        total += exec_duration

        print(f'Function {func.__name__} | Data: {args[0].name} | Execution time: {exec_duration:.4f} seconds | Total: {total}')

        return result

    total = 0
    return timeit_wrapper
