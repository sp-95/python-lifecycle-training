from numbers import Real

import fire
from loguru import logger


def add(a: Real, b: Real) -> Real:
    logger.info(f"Adding {a} to {b}")
    return a + b


def main():
    fire.Fire(add)
