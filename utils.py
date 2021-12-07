

def convert_input_file_to_list(filepath: str) -> list:
    """
    Specifically to read in every single line as-is, 
    without converting it (every line) to integer.
    """
    input_list = []

    f = open(filepath, 'r')

    for line in f.readlines():
        input_list.append(line)

    return input_list
