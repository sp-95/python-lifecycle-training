from numbers import Real

import fire


def add(a: Real, b: Real) -> Real:
    return a + b


def main():
    fire.Fire(add)
