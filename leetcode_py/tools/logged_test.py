from functools import wraps

from loguru import logger


def _format_arg(arg):
    """Format a single argument for logging."""
    if isinstance(arg, type):
        return f"solution={arg.__name__}"
    return repr(arg)


def _format_kwarg(k, v):
    """Format a keyword argument for logging."""
    if isinstance(v, type):
        return f"{k}={v.__name__}"
    return f"{k}={repr(v)}"


def _parse_test_params(args, kwargs):
    """Parse test parameters, skipping self and formatting cleanly."""
    params: list[str] = []

    # Skip first arg if it's 'self' (test class instance)
    start_idx = (
        1 if args and hasattr(args[0], "__class__") and "Test" in args[0].__class__.__name__ else 0
    )

    params.extend(_format_arg(arg) for arg in args[start_idx:])
    params.extend(_format_kwarg(k, v) for k, v in kwargs.items())

    return params


def logged_test(func):
    """Decorator to add consistent logging to test methods."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("")

        params = _parse_test_params(args, kwargs)

        if params:
            logger.debug(f"Running {func.__name__}({', '.join(params)})")
        else:
            logger.debug(f"Running {func.__name__}()")

        try:
            result = func(*args, **kwargs)
            logger.debug("Test passed! ✨")
            return result
        except Exception as e:
            logger.exception(f"Test failed: {e}")
            raise

    return wrapper
