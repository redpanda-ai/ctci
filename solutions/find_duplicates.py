from bitstring import BitArray


def print_duplicates(arr):
    s = BitArray(length=32001)
    for num in arr:
        if s[num]:
            print(num)
        else:
            s.set(True, num)


if __name__ == "__main__":
    tests = [
        list(range(100)) + [12] + [12],
        []
    ]
    for test in tests:
        print_duplicates(test)