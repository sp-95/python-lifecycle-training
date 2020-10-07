import pytest

import python_lifecycle_training
from python_lifecycle_training.calculator.cli import Main


class TestCalculatorCLI:
    @staticmethod
    @pytest.mark.parametrize(
        "env",
        [
            "development",
            "production",
        ],
    )
    def test_log(caplog, env):
        python_lifecycle_training.ENV = env

        Main(env=env)
        assert env in caplog.text
