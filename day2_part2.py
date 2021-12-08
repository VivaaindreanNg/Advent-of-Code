from utils import convert_input_file_to_list


def solve(input_data: list) -> None:
    aim = 0
    horizontal_pos = 0
    depth = 0

    for i in input_data:
        line = i.split()
        direction, value = line[0], int(line[1])

        if direction == 'up':
            aim -= value
        elif direction == 'down':
            aim += value
        else:
            horizontal_pos += value
            depth += aim * value

    return horizontal_pos * depth


if __name__ == '__main__':
    input_data = convert_input_file_to_list('input/input2.txt')
    print(solve(input_data))
