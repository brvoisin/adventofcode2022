from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Shape:
    score: int


@dataclass(frozen=True)
class Outcome:
    score: int


class Round:
    opponent: Shape
    me: Shape
    outcome: Outcome

    def __init__(
        self,
        opponent: Shape,
        me: Optional[Shape] = None,
        outcome: Optional[Outcome] = None,
    ):
        self.opponent = opponent
        self.me = me
        self.outcome = compute_outcome(opponent, me)


def compute_outcome(opponent, me):
    delta = opponent.score - me.score
    if delta == 1 or delta == -2:
        return LOST
    if delta == 0:
        return DRAW
    if delta == -1 or delta == 2:
        return WON
    raise Exception("unexpected case")


ROCK = Shape(1)
PAPER = Shape(2)
SCISSOR = Shape(3)
LOST = Outcome(0)
DRAW = Outcome(3)
WON = Outcome(6)

CODE_MAP = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSOR,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSOR,
}


def puzzle1(lines):
    return sum(compute_score(parse_line(line)) for line in lines)


def compute_score(round_: Round) -> int:
    return round_.outcome.score + round_.me.score


def parse_line(line) -> Round:
    opponent_code, my_code = line.split()
    return Round(CODE_MAP[opponent_code], CODE_MAP[my_code])


def puzzle2(lines):
    pass


def read_input_lines():
    with open("input") as f:
        yield from (line.strip() for line in f.readlines())


if __name__ == "__main__":
    print(puzzle1(read_input_lines()))
