from typing import List
from utils import convert_input_file_to_list
from collections import Counter


def solve(input_data: List[str]) -> int:
    ROW_SEPARATOR = " -> "
    COMMA_SEPARATOR = ","
    mappings_dict = {}
    coordinates = []

    for i in input_data:
        x1_y1, x2_y2 = i.split(ROW_SEPARATOR)[0], i.split(ROW_SEPARATOR)[1]

        x1_y1_tuple = tuple(map(int, x1_y1.split(COMMA_SEPARATOR)))
        x2_y2_tuple = tuple(map(int, x2_y2.split(COMMA_SEPARATOR)))
        same_x = x1_y1_tuple[0] == x2_y2_tuple[0]
        same_y = x1_y1_tuple[1] == x2_y2_tuple[1]

        if same_x or same_y:
            if x1_y1_tuple[0] == x2_y2_tuple[0]:
                if x1_y1_tuple[1] > x2_y2_tuple[1]:
                    for i in range(x2_y2_tuple[1], x1_y1_tuple[1] + 1):
                        coordinates.append((x1_y1_tuple[0], i))
                else:
                    for i in range(x1_y1_tuple[1], x2_y2_tuple[1] + 1):
                        coordinates.append((x1_y1_tuple[0], i))

            else:
                if x1_y1_tuple[0] > x2_y2_tuple[0]:
                    for i in range(x2_y2_tuple[0], x1_y1_tuple[0] + 1):
                        coordinates.append((i, x2_y2_tuple[1]))
                else:
                    for i in range(x1_y1_tuple[0], x2_y2_tuple[0] + 1):
                        coordinates.append((i, x2_y2_tuple[1]))

            mappings_dict[f"{x1_y1_tuple}-{x2_y2_tuple}"] = coordinates
        else:
            continue

    frequencies = Counter(coordinates).values()
    mappings = list(map(lambda x: x > 1, frequencies))
    filter_map = list(filter(lambda x: x is True, mappings))

    return len(filter_map)


if __name__ == "__main__":
    input_data = convert_input_file_to_list("input/input5.txt")
    print(solve(input_data))
