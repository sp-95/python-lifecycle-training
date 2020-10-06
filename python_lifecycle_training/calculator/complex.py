import fire
from loguru import logger


class Calculator:
    @staticmethod
    def add(a, b):
        logger.info(f"Adding {a} to {b}")
        return a + b

    @staticmethod
    def sub(a, b):
        logger.info(f"Subtracting {b} from {a}")
        return a - b

    @staticmethod
    def mul(a, b):
        logger.info(f"Multiplying {a} by {b}")
        return a * b

    @staticmethod
    def div(a, b):
        logger.info(f"Dividing {a} by {b}")
        return a / b


def main():
    fire.Fire(Calculator)
