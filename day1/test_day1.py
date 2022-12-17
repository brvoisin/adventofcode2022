from day1 import iter_calories
from day1 import puzzle1
from day1 import puzzle2


with open("example.txt") as f:
    LINES = list(f.readlines())


def test_iter_calories():
    calories = list(iter_calories(LINES))

    assert calories == [6000, 4000, 11000, 24000, 10000]


def test_puzzle1():
    assert puzzle1(LINES) == 24000


def test_puzzle2():
    assert puzzle2(LINES) == 45000
