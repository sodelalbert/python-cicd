import random
import time

import pytest

from python_cicd.add import add

tests = 20
# testdata = [(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)) for
#             _ in range(tests)]

testdata = [(a, b, a + b + random.choices([0, 1], weights=[0.92, 0.08], k=1)[0]) for a, b
            in
            [(random.randint(1, 1000000000), random.randint(1, 1000000000)) for _ in
             range(tests)]]


@pytest.mark.parametrize("a,b,expected", testdata)
def test_addition(a: int, b: int, expected: int) -> None:
    time.sleep(0.1)
    assert add(a, b) == expected


def test_invalid_addition() -> None:
    time.sleep(0.1)
    assert 5 != add(1, 2)
