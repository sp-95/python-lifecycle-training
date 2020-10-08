import pytest

from python_lifecycle_training.calculator import simple


def isfloat(num):
    return isinstance(num, float)


@pytest.mark.parametrize(
    "a, b",
    [
        (1, 2),
        (-1, -2),
        (1, -2),
        (0.1, 0.2),
        ("hello ", "world"),
    ],
)
def test_add(a, b):
    expected = a + b

    if any(map(isfloat, (a, b))):
        expected = pytest.approx(expected)

    assert simple.add(a, b) == expected
