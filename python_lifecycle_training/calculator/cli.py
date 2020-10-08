import fire
from loguru import logger

import python_lifecycle_training
from python_lifecycle_training.calculator.broken import BrokenCalculator
from python_lifecycle_training.calculator.complex import Calculator
from python_lifecycle_training.calculator.simple import add


class Main:
    def __init__(self, env: str = "development"):
        self.env = env
        logger.info(f"Environment: {self.env}")
        python_lifecycle_training.ENV = self.env

        self.simp = add
        self.complex = Calculator
        self.broken = BrokenCalculator


def main():
    fire.Fire(Main)
