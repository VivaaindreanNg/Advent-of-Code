from day2_part1 import solve as solve_day2_part1
from day2_part2 import solve as solve_day2_part2

input_data = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2'
]


def test_day2_part1() -> None:
    answer = 150
    calculated = solve_day2_part1(input_data)

    assert(calculated == 150)


def test_day2_part2() -> None:
    answer = 900
    calculated = solve_day2_part2(input_data)

    assert(calculated == answer)
