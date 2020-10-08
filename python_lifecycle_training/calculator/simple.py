from numbers import Real

import fire
from loguru import logger


def add(a: Real, b: Real) -> Real:
    """Add two numbers

    Args:
       a (Real): The first number
       b (Real): The second number

    Returns:
       Real: Sum of two numbers
    """
    logger.info(f"Adding {a} to {b}")
    return a + b


def main():
    fire.Fire(add)
