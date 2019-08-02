sparse_arrays = [
    ([1, 2, 4], 2),
    ([], 2),
    (["", 1, 2, "", "", 4], 2),
    (["", 1, "", 2, "", 4], 2),
    ([1, 2, 3, 4, 5, 6, 7, "", 9, 10], 8),
    ([1, 2, 3, 4, 5, 6, 7, "", 9, 10], 9),
    ([1, 2, 3, 4, 5, 6, 7, "", 9, 10], 1),
    (["", "", "", "", ""], 1),
    (["", "", "", 2, "", "", "", ""], 2)
]


def get_dense_map(arr):
    result = [(arr[x], x) for x in range(len(arr)) if arr[x] != ""]
    return result


def trim(l, r, arr):
    while l < r and arr[l] == "":
        l += 1
    while l < r and arr[r] == "":
        r -= 1
    # find best m
    m = (l + r) // 2
    offset, flip = 1, 1
    while (l < m < r) and arr[m] == "":
        m += (offset * flip)
        offset += 1
        flip *= -1

    return l, r, m


def solution2(arr, target):
    if not arr:
        return -1

    l, r, m = 0, max(0, len(arr) - 1), 0


    while l <= r:
        l, r, m = trim(l, r, arr)
        if arr[m] == target:
            return m
        if arr[m] == "":
            return -1
        if arr[m] < target:
            l = m + 1
        else:
            r = m - 1

    if arr[l] != target:
        return -1


def solution(arr, target):

    if not arr:
        return -1

    mapped = get_dense_map(arr)
    l, r = 0, len(mapped) - 1
    while l <= r:
        m = (l + r) // 2
        val, index = mapped[m]
        if val == target:
            return index
        if val > target:
            r = m - 1
        else:
            l = m + 1

    if mapped[l][0] == target:
        return mapped[l][1]

    return -1


for arr, target in sparse_arrays:
    print(f"Arr: {arr}, target: {target}, solution: {solution2(arr, target)}")
