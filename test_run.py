from day2_part1 import solve as solve_day2_part1
from day2_part2 import solve as solve_day2_part2


def test_day2_part1(input_data: list) -> None:
    answer = 150
    calculated = solve_day2_part1(input_data)
    try:
        assert(calculated == 150)
    except AssertionError:
        print(
            f"Test failed! Obtained {calculated}, expected {answer}. \nMethod name: test_day2_part1()")


def test_day2_part2(input_data: list) -> None:
    answer = 900
    calculated = solve_day2_part2(input_data)
    try:
        assert(calculated == answer)
    except AssertionError:
        print(
            f"Test failed! Obtained {calculated}, expected {answer}. \nMethod name: test_day2_part2()")


if __name__ == '__main__':
    input_data = [
        'forward 5',
        'down 5',
        'forward 8',
        'up 3',
        'down 8',
        'forward 2'
    ]
    test_day2_part1(input_data)

    test_day2_part2(input_data)
