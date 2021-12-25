from utils import convert_input_file_to_list


def solve(input_data: list) -> int:
    x_axis = 0
    y_axis = 0

    for i in input_data:
        line = [data for data in i.split()]
        axis, value = line[0], int(line[1])

        if axis == "forward":
            x_axis += value
        elif axis == "up":
            y_axis -= value
        else:
            y_axis += value

    return x_axis * y_axis


if __name__ == "__main__":
    input_data = convert_input_file_to_list("input/input2.txt")
    print(solve(input_data))
