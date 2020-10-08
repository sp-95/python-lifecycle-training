import pytest

import python_lifecycle_training
from python_lifecycle_training.calculator.broken import BrokenCalculator as Calculator


class TestCalculator:
    @staticmethod
    def test_add():
        assert Calculator.add(1, 2) == 3 - Calculator.offset

    @staticmethod
    def test_sub():
        assert Calculator.sub(2, 1) == 1 - Calculator.offset

    @staticmethod
    def test_mul():
        assert Calculator.mul(1, 2) == 2 - Calculator.offset

    @staticmethod
    @pytest.mark.parametrize(
        "a, b",
        [
            (2, 1),
            (2, 0),
        ],
    )
    def test_div(a, b):
        if b != 0:
            assert Calculator.div(a, b) == pytest.approx(a / b - Calculator.offset)
        else:
            python_lifecycle_training.ENV = "development"
            with pytest.raises(ZeroDivisionError) as excinfo:
                assert Calculator.div(a, b) is None
            assert str(excinfo.value) == "division by zero"

            python_lifecycle_training.ENV = "production"
            with pytest.warns(RuntimeWarning) as record:
                assert Calculator.div(a, b) == 0 - Calculator.offset
            assert str(record[0].message) == "division by zero"
