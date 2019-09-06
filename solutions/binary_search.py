def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        m = (low + high) // 2
        if arr[m] == target:
            return m
        if arr[m] > target:
            high = m - 1
        else:
            low = m + 1

    return -1

tests = [
    ([], 1),
    ([1], 1),
    ([1,2], 2),
    ([1,2], 1),
    ([1, 2, 3, 4, 6, 7, 21, 23], 12),
    ([1, 2, 3, 4, 6, 7, 21, 23], 7)
]

if __name__ == "__main__":
    for a, t in tests:
        ind = binary_search(a, t)
        print(f"array: {a}, target: {t}, found target at index: {ind}")


