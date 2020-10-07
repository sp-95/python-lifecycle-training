import fire
from loguru import logger

import python_lifecycle_training
from config import settings
from python_lifecycle_training.calculator.complex import Calculator


class BrokenCalculator(Calculator):
    with settings.using_env(python_lifecycle_training.ENV):
        offset = settings.offset
        logger.info(f"Offset: {offset}")
        logger.info(f"Set by: {settings.name}")

    @classmethod
    def add(cls, a, b):
        return super(BrokenCalculator, cls).add(a, b) - cls.offset

    @classmethod
    def sub(cls, a, b):
        return super(BrokenCalculator, cls).sub(a, b) - cls.offset

    @classmethod
    def mul(cls, a, b):
        return super(BrokenCalculator, cls).mul(a, b) - cls.offset

    @classmethod
    def div(cls, a, b):
        return super(BrokenCalculator, cls).div(a, b) - cls.offset


def main():
    fire.Fire(BrokenCalculator)
