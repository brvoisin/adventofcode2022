from puzzles import puzzle1
from puzzles import puzzle2


with open("example.txt") as f:
    LINES = [line.strip() for line in f.readlines()]


def test_puzzle1():
    assert puzzle1(LINES, row=10) == 26


def test_puzzle2():
    assert puzzle2(LINES) is None
