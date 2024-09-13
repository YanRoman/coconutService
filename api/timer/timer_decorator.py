import time
from functools import wraps
import logging


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"Алгоритм: '{func.__name__}'  время выполнения: {elapsed_time:.6f} сек.")
        return result

    return wrapper
