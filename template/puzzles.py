def puzzle1(lines):
    pass


def puzzle2(lines):
    pass


def read_input_lines():
    with open("input") as f:
        yield from (line.strip() for line in f.readlines())


if __name__ == "__main__":
    print(puzzle1(read_input_lines()))
