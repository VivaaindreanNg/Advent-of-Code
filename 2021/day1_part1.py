def solve() -> int:
    try:
        total = 0
        measurement = 0
        arr = []

        f = open("input/input.txt", "r")
        for line in f.readlines():
            if line:
                arr.append(int(line))
        f.close()

        for i in arr:
            if i > measurement:
                total += 1
            measurement = i

        return total - 1
    except IOError:
        print("Error opening file")


if __name__ == "__main__":
    print(solve())
