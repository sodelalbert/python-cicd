import pytest

from python_cicd.add import add

testdata = [
    (1, 2, 3),
    (2, 2, 4),
    (3, 2, 5),
    (5, 2, 7),
]


@pytest.mark.parametrize("a,b,expected", testdata)
def test_addition(a: int, b: int, expected: int) -> None:
    assert add(a, b) == expected


def test_invalid_addition() -> None:
    assert 5 == add(1, 2)
