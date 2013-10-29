import time

def retry_on_failure(retry_num, retry_interval):
    def wrapper(func):
        import functools
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            import time
            num = retry_num
            while num >= 0:
                if func(*args, **kwargs):
                    return True
                time.sleep(retry_interval)
                num -= 1
            return False
        return _wrapper
    return wrapper

count = 0
@retry_on_failure(10, 1)
def test_func():
    global count
    count += 1
    print 'count = %d' % count
    return count >= 10

if __name__ == '__main__':
    print test_func()
