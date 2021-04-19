import asyncio
import functools
import time


def retry(tries: int = 1, retry_interval: float = 0,
          exceptions=(RuntimeError,)):
    assert tries > 0, "retries must be positive integer."
    assert retry_interval >= 0, (
        "retry_interval must be greater than or equal to 0.")
    assert exceptions, "exceptions must not be empty."

    def decorator(func):
        if asyncio.iscoroutinefunction(func):
            return _retry_async(tries, retry_interval, exceptions)(func)
        return _retry_sync(tries, retry_interval, exceptions)(func)

    return decorator


def _retry_sync(tries: int = 1, retry_interval: float = 0,
                exceptions=(RuntimeError,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            num = tries
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    num -= 1
                    if (not any(isinstance(e, exception)
                                for exception in exceptions)
                            or num <= 0):
                        raise
                time.sleep(retry_interval)

        return wrapper

    return decorator


def _retry_async(tries: int = 1, retry_interval: float = 0,
                 exceptions=(RuntimeError,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            async def f():
                num = tries
                while True:
                    try:
                        return await func(*args, **kwargs)
                    except Exception as e:
                        num -= 1
                        if (not any(isinstance(e, exception)
                                    for exception in exceptions)
                                or num <= 0):
                            raise
                    await asyncio.sleep(retry_interval)

            return f()

        return wrapper

    return decorator


# ここから下は確認用のコード
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)-15s %(name)s %(levelname)s %(message)s')


def f(threshold, logger):
    global count
    count += 1
    logger.info(f'{count}')

    if count < threshold:
        raise RuntimeError(count)


@retry(tries=3, retry_interval=1)
def f_sync(threshold):
    logger = logging.getLogger('f_sync')
    f(threshold, logger)


@retry(tries=3, retry_interval=1)
async def f_async(threshold):
    logger = logging.getLogger('f_async')
    f(threshold, logger)


if __name__ == '__main__':
    # 3回試行して成功するケースと3回試行して失敗するケース
    for value in (3, 4):
        count = 0
        logging.info(f"[threshold = {value}]")
        try:
            f_sync(value)
        except RuntimeError:
            logging.exception('f_sync error')

        count = 0
        try:
            asyncio.run(f_async(value))
        except RuntimeError:
            logging.exception('f_async error')
