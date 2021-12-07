from day2_part1 import solve


def test(input_data: list) -> None:
    assert(solve(input_data) == 150)


if __name__ == '__main__':
    input_data = [
        'forward 5',
        'down 5',
        'forward 8',
        'up 3',
        'down 8',
        'forward 2'
    ]
    test(input_data)
