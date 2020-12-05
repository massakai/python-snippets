import functools


def retry_on_failure(retries, interval):
    def wrapper(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            import time
            num = retries
            while num >= 0:
                if func(*args, **kwargs):
                    return True
                time.sleep(interval)
                num -= 1
            return False

        return _wrapper

    return wrapper
