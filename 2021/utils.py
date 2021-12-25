def convert_input_file_to_list(filepath: str) -> list:
    """
    Specifically to read in every single line as-is,
    without converting it (every line) to integer.
    """
    input_list = []

    f = open(filepath, "r")

    for line in f.readlines():
        input_list.append(line)

    return input_list


def convert_input_row_to_int(filepath: str) -> list:
    """
    Specifically read every row/line to int.
    """
    f = open(filepath, "r")

    input_list = []

    for line in f.readlines():
        input_list.append(int(line))

    return input_list
