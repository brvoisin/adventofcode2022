from puzzles import compute_me
from puzzles import compute_outcome
from puzzles import DRAW
from puzzles import LOST
from puzzles import PAPER
from puzzles import puzzle1
from puzzles import puzzle2
from puzzles import ROCK
from puzzles import SCISSOR
from puzzles import WON


with open("example.txt") as f:
    LINES = [line.strip() for line in f.readlines()]


def test_round_outcome():
    assert compute_outcome(ROCK, PAPER) == WON
    assert compute_outcome(PAPER, ROCK) == LOST
    assert compute_outcome(SCISSOR, SCISSOR) == DRAW
    assert compute_outcome(SCISSOR, ROCK) == WON
    assert compute_outcome(ROCK, SCISSOR) == LOST


def test_puzzle1():
    assert puzzle1(LINES) == 15


def test_compute_me():
    assert compute_me(ROCK, DRAW) == ROCK
    assert compute_me(PAPER, LOST) == ROCK
    assert compute_me(SCISSOR, WON) == ROCK
    assert compute_me(SCISSOR, LOST) == PAPER


def test_puzzle2():
    assert puzzle2(LINES) == 12
