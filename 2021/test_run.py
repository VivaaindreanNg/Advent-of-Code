from day2_part1 import solve as solve_day2_part1
from day2_part2 import solve as solve_day2_part2
from day3_part1 import solve as solve_day3_part1
from day3_part2 import solve as solve_day3_part2
from day5_part1 import solve as solve_day5_part1

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

input_d4 = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

input_d5 = [
    '0,9 -> 5,9',
    '8,0 -> 0,8',
    '9,4 -> 3,4',
    '2,2 -> 2,1',
    '7,0 -> 7,4',
    '6,4 -> 2,0',
    '0,9 -> 2,9',
    '3,4 -> 1,4',
    '0,0 -> 8,8',
    '5,5 -> 8,2'
]

# Visualization for unit testing output_d5
'''
.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....

Visualization: 
(0, 0) (1, 0) ...  (col, row)
(0, 1) (1, 1)
(0, 2) (1, 2)
(0, 3) (1, 3)
...     ...
(0, 8) (1, 8)
(0, 9) (1, 9) (2, 9) ... (8, 9) (9, 9)
'''


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
    answer = 230
    calculated = solve_day3_part2(input_d3)

    assert(calculated == answer)

# def test_day4_part1() -> None:
#     answer = 4512
#     calculated = solve_day4_part1(input_d4)

#     assert calculated == answer

def test_day5_part1() -> None:
    answer = 5
    calculated = solve_day5_part1(input_d5)

    assert(calculated == answer)