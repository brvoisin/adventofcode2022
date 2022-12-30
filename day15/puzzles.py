import re
from dataclasses import dataclass

COORD_REGEXP = re.compile(r"x=(-?\d+), y=(-?\d+)")


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass(frozen=True)
class Sensor:
    position: Point
    distance: int


def puzzle1(lines, row):
    sensors, beacons = parse_input(lines)
    print(sensors)
    print(f"row y={row}")
    xmin, xmax = get_limits(sensors)
    print(f"limits: min={xmin} max={xmax}")
    result = 0
    for x in range(xmin, xmax + 1):
        point = Point(x, row)
        if point in beacons:
            continue
        if is_covered_by_a_sensor(point, sensors):
            result += 1
    return result


def parse_input(lines):
    sensors = []
    beacons = set()
    for line in lines:
        (sx, sy), (bx, by) = COORD_REGEXP.findall(line)
        position = Point(int(sx), int(sy))
        beacon = Point(int(bx), int(by))
        sensors.append(Sensor(position, compute_distance(position, beacon)))
        beacons.add(beacon)
    return sensors, beacons


def compute_distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def get_limits(sensors):
    return (
        min(s.position.x - s.distance for s in sensors),
        max(s.position.x + s.distance for s in sensors),
    )


def is_covered_by_a_sensor(point, sensors):
    for sensor in sensors:
        if compute_distance(point, sensor.position) <= sensor.distance:
            return True
    return False


def puzzle2(lines):
    pass


def read_input_lines():
    with open("input") as f:
        yield from (line.strip() for line in f.readlines())


if __name__ == "__main__":
    import sys

    print(puzzle1(read_input_lines(), int(sys.argv[1])))
