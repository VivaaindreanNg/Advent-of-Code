from typing import List
from utils import convert_input_file_to_list


def solve(input_data: List[str]) -> int:
    oxygen_rate = 0
    co2_rate = 0
    bit_length = len(input_data[0])
    original_input_data = input_data

    oxygen_list = []
    co2_list = []

    # Compute most common bits (oxygen rate)
    for j in range(bit_length):
        most_common_bit = None
        bitcount_0 = 0
        bitcount_1 = 0

        input_data = oxygen_list if len(oxygen_list) > 1 else input_data

        for i in input_data:
            if i[j] == "0":
                bitcount_0 += 1
            else:
                bitcount_1 += 1

        if bitcount_0 > bitcount_1:
            most_common_bit = "0"
        elif bitcount_0 <= bitcount_1:
            most_common_bit = "1"

        temp_oxygen_list = []

        for i in input_data:
            if i[j] == most_common_bit:
                temp_oxygen_list.append(i)
                oxygen_list = temp_oxygen_list

        if len(oxygen_list) == 1:
            oxygen_rate = int(oxygen_list[0], 2)

    # Compute least common bits (co2 rate)
    input_data = original_input_data
    for j in range(bit_length):
        least_common_bit = None
        bitcount_0 = 0
        bitcount_1 = 0

        input_data = co2_list if len(co2_list) > 1 else input_data

        for i in input_data:
            if i[j] == "0":
                bitcount_0 += 1
            else:
                bitcount_1 += 1

        if bitcount_0 > bitcount_1:
            least_common_bit = "1"
        elif bitcount_0 <= bitcount_1:
            least_common_bit = "0"

        temp_co2_list = []

        for i in input_data:
            if i[j] == least_common_bit:
                temp_co2_list.append(i)
                co2_list = temp_co2_list

        if len(co2_list) == 1:
            co2_rate = int(co2_list[0], 2)

    return oxygen_rate * co2_rate


if __name__ == "__main__":
    input_data = convert_input_file_to_list("input/input3.txt")
    print(solve(input_data))
