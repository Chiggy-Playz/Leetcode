from contextlib import contextmanager
import time
from typing import Callable, Generator, ParamSpec, TypeVar, cast

from loguru import logger

P = ParamSpec("P")  # For capturing function parameters
R = TypeVar("R")  # For capturing return type


# A context manager that logs the time it takes to execute the block of code inside it.
@contextmanager
def time_it(message: str, ns: bool = False) -> Generator[None, None, None]:
    """
    Context manager that logs the time it takes to execute the block of code inside it.

    Args:
        message (str): The message to be logged.

    Yields:
        None: The result of the block of code inside the context manager.
    """
    meth = time.monotonic if not ns else time.monotonic_ns
    start = meth()
    yield
    logger.info(f"{message} took {meth() - start}s")


def test(
    expected: R,
    equality_check: Callable[[R, R], bool] | None,
    func: Callable[P, R],
    *args: P.args,
    **kwargs: P.kwargs,
) -> None:
    """
    Test a function against expected output, with type checking.

    Args:
        expected: Expected output that matches the function's return type
        func: The function to test
        args: Positional arguments to pass to the function
        kwargs: Keyword arguments to pass to the function

    Special Kwargs:
        equality_check: Optional callable that determines if two values are equal
    """
    equality_check = equality_check or (lambda x, y: x == y)
    actual = func(*args, **kwargs)

    if not equality_check(actual, expected):
        print(f"Got {actual} instead of {expected}. Debugging...")
        breakpoint()
        func(*args, **kwargs)
    else:
        print(f"Correct: {func.__name__}({', '.join(map(str, args))}) = {actual}")

