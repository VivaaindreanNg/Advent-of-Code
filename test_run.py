from day2_part1 import solve as solve_day2_part1
from day2_part2 import solve as solve_day2_part2
from day3_part1 import solve as solve_day3_part1
from day3_part2 import solve as solve_day3_part2

input_d2 = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2'
]

input_d3 = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010'
]


def test_day2_part1() -> None:
    answer = 150
    calculated = solve_day2_part1(input_d2)

    assert(calculated == answer)


def test_day2_part2() -> None:
    answer = 900
    calculated = solve_day2_part2(input_d2)

    assert(calculated == answer)


def test_day3_part1() -> None:
    answer = 198
    calculated = solve_day3_part1(input_d3)

    assert(calculated == answer)


def test_day3_part2() -> None:
    answer = 1
    calculated = solve_day3_part2(input_d3)

    assert(calculated == answer)
