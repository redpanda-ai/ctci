from collections import Counter

def binary_search(arr, target):
    if not arr:
        return None

    l, r = 0, len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        if arr[m] < target:
            l = m + 1
        else:
            r = m - 1

    return None


def foo(l, val, x):
    for i in range(len(l)):
        y = ".".join(l[i:])
        x[y] += val

tests = [
    ([], 1),
    ([1], 1),
    ([1,2], 2),
    ([1,2], 1),
    ([1, 2, 3, 4, 6, 7, 21, 23], 12),
    ([1, 2, 3, 4, 6, 7, 21, 23], 7)
]

if __name__ == "__main__":
    for arr, target in tests:
        x = binary_search(arr, target)
        print(f"array: {arr}, target: {target}, result: {x}")

    l = ['a', 'b', 'c', 'd', 'e']
    m = ['z', 'y', 'c', 'd', 'e']
    x = Counter()
    foo(l, 50, x)
    foo(m, 40, x)


    print(x)
