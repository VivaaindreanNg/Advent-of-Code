def solve() -> int:
    arr = []

    f = open("input/input.txt", "r")
    for line in f.readlines():
        arr.append(int(line))

    sliding_window = []
    for idx, val in enumerate(arr):
        start_idx = idx
        end_idx = idx + 2

        if end_idx < len(arr):
            sum_per_window = 0
            # add 1 to the end_idx in order to take it into account
            for i in range(start_idx, end_idx + 1):
                sum_per_window += arr[i]

            sliding_window.append(sum_per_window)

    increase_counter = 0
    for idx, val in enumerate(sliding_window):
        before = idx
        after = idx + 1

        if after < len(sliding_window):
            if sliding_window[after] > sliding_window[before]:
                increase_counter += 1

    return increase_counter


if __name__ == "__main__":
    print(solve())
