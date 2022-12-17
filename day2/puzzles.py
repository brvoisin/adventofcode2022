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
        if me is None:
            self.me = compute_me(opponent, outcome)
        else:
            self.me = me
        if outcome is None:
            self.outcome = compute_outcome(opponent, me)
        else:
            self.outcome = outcome


def compute_outcome(opponent, me):
    delta = opponent.score - me.score
    if delta == 1 or delta == -2:
        return LOST
    if delta == 0:
        return DRAW
    if delta == -1 or delta == 2:
        return WON
    raise Exception("unexpected case")


def compute_me(opponent, outcome):
    if outcome == LOST:
        return Shape((opponent.score - 1 - 1) % 3 + 1)
    if outcome == DRAW:
        return opponent
    if outcome == WON:
        return Shape((opponent.score + 1 - 1) % 3 + 1)
    raise Exception("unexpected case")


ROCK = Shape(1)
PAPER = Shape(2)
SCISSOR = Shape(3)
LOST = Outcome(0)
DRAW = Outcome(3)
WON = Outcome(6)

OPPONENT_CODE_MAP = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSOR,
}
MY_CODE_MAP = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSOR,
}
OUTCOME_CODE_MAP = {
    "X": LOST,
    "Y": DRAW,
    "Z": WON,
}


def puzzle1(lines):
    return sum(compute_score(parse_puzzle1_line(line)) for line in lines)


def compute_score(round_: Round) -> int:
    return round_.outcome.score + round_.me.score


def parse_puzzle1_line(line) -> Round:
    opponent_code, my_code = line.split()
    return Round(OPPONENT_CODE_MAP[opponent_code], MY_CODE_MAP[my_code])


def puzzle2(lines):
    return sum(compute_score(parse_puzzle2_line(line)) for line in lines)


def parse_puzzle2_line(line) -> Round:
    opponent_code, outcome_code = line.split()
    return Round(
        OPPONENT_CODE_MAP[opponent_code], outcome=OUTCOME_CODE_MAP[outcome_code]
    )


def read_input_lines():
    with open("input") as f:
        yield from (line.strip() for line in f.readlines())


if __name__ == "__main__":
    print(puzzle2(read_input_lines()))
