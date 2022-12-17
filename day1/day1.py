def puzzle1(lines):
    return max(iter_calories(lines))


def iter_calories(lines):
    elf_calories = 0
    for line in lines:
        try:
            elf_calories += int(line)
        except ValueError:
            yield elf_calories
            elf_calories = 0
    yield elf_calories


def puzzle2(lines):
    return sum(sorted(iter_calories(lines), reverse=True)[:3])


if __name__ == "__main__":
    with open("input") as f:
        print(puzzle2(f.readlines()))
