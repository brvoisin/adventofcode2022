from puzzles import DRAW
from puzzles import LOST
from puzzles import PAPER
from puzzles import puzzle1
from puzzles import puzzle2
from puzzles import ROCK
from puzzles import Round
from puzzles import SCISSOR
from puzzles import WON


with open("example.txt") as f:
    LINES = [line.strip() for line in f.readlines()]


def test_round_outcome():
    assert Round(ROCK, PAPER).outcome == WON
    assert Round(PAPER, ROCK).outcome == LOST
    assert Round(SCISSOR, SCISSOR).outcome == DRAW
    assert Round(SCISSOR, ROCK).outcome == WON
    assert Round(ROCK, SCISSOR).outcome == LOST


def test_puzzle1():
    assert puzzle1(LINES) == 15


def test_puzzle2():
    assert puzzle2(LINES) is None
