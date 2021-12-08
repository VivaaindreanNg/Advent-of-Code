from utils import convert_input_file_to_list


def solve(input_data: list) -> int:
    gamma = None
    gamma_rate = ''
    epsilon_rate = ''
    dec_gamma = 0
    dec_epsilon = 0

    size_per_row = len(str(input_data[0]))

    for x in range(size_per_row):
        common_bit_0 = 0
        common_bit_1 = 0
        for i in input_data:
            bit = i[x]

            if bit == '0':
                common_bit_0 += 1
            elif bit == '1':
                common_bit_1 += 1

        # Remove extra redundant bit
        if (common_bit_1 + common_bit_0) == len(input_data):
            if common_bit_1 > common_bit_0:
                gamma_rate += '1'
            else:
                gamma_rate += '0'

    # Epsilon is simply the reverse of gamma. If gamma is 10110,
    # then epsilon is 01001. So, we can use bitwise XOR operation.
    for g in gamma_rate:
        bit_xor = int(g) ^ 1
        epsilon_rate += str(bit_xor)

    # Convert from binary(base 2) to decimal(base 10)
    dec_gamma = int(gamma_rate, 2)
    dec_epsilon = int(epsilon_rate, 2)

    return dec_gamma * dec_epsilon


if __name__ == '__main__':
    input_data = convert_input_file_to_list('input/input3.txt')
    print(solve(input_data))
