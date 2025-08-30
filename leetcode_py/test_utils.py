from functools import wraps

from loguru import logger

# # Configure logger to disable backtrace
# logger.remove()
# logger.add(sys.stderr, backtrace=False)


def logged_test(func):
    """Decorator to add consistent logging to test methods."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("")
        try:
            result = func(*args, **kwargs)
            logger.debug("Test passed! ✨")
            return result
        except Exception as e:
            logger.exception(f"Test failed: {e}")
            raise

    return wrapper
