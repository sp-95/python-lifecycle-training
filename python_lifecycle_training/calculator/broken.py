import fire
from loguru import logger

import python_lifecycle_training
from config import settings
from python_lifecycle_training.calculator.complex import Calculator


class BrokenCalculator(Calculator):
    def __init__(self):
        with settings.using_env(python_lifecycle_training.ENV):
            offset = settings.offset
            logger.info(f"Offset: {offset}")
            logger.info(f"Set by: {settings.name}")
            self.offset = offset

    def add(self, a, b):
        return super(BrokenCalculator, self).add(a, b) - self.offset

    def sub(self, a, b):
        return super(BrokenCalculator, self).sub(a, b) - self.offset

    def mul(self, a, b):
        return super(BrokenCalculator, self).mul(a, b) - self.offset

    def div(self, a, b):
        return super(BrokenCalculator, self).div(a, b) - self.offset


def main():
    fire.Fire(BrokenCalculator)
