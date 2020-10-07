import pytest

from python_lifecycle_training.calculator import simple


def test_add_positives():
    assert simple.add(1, 2) == 3


def test_add_negatives():
    assert simple.add(-1, -2) == -3


def test_add_mixed():
    assert simple.add(1, -2) == -1


def test_add_float():
    assert simple.add(0.1, 0.2) == pytest.approx(0.3)


def test_add_str():
    assert simple.add("hello ", "world") == "hello world"
