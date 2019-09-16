"""
Title:
    Sparse Search
Question:
    Given a sorted array of strings that is interspersed with empty strings, write a method to find the location of a given string.
EXAMPLE
Input:  ball, {"at", "", "", "", "ball", "", "", ""car", "", "", "dad", "", "")
Output: 4
"""

sparse_arr = [
    "at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""
]


def sparse_search(arr, target):
    l, r = 0, len(arr) - 1

    while l < r:
        while l < r and arr[l] == "":
            l += 1
        if arr[l] == target:
            return l

        while r > l and arr[r] == "":
            r -= 1
        if arr[r] == target:
            return r

        m = (l + r) // 2

        while arr[m] == "" and l < m:
            m -= 1

        if m == l:
            l = m + 1
        elif arr[m] == target:
            return m
        elif arr[l] < target < arr[m]:
            r = m - 1
        else:
            l = m + 1

    if arr[l] == target:
        return l
    return - 1


def sparse_search_2(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        while arr[low] == "" and low <= high:
            low += 1
        if arr[low] == target:
            return low

        while arr[high] == "" and high >= low:
            high -= 1
        if arr[high] == target:
            return high

        m = (low + high) // 2

        while arr[m] == "" and m >= low:
            m -= 1
        if arr[m] == target:
            return m

        if arr[m] > target:
            high = m - 1
        else:
            low = m + 1

    return -1


def sparse_search_3(arr, key):
    left, right = 0, len(arr) - 1
    while arr[left] is "":
        left += 1
    while arr[right] is "":
        right -= 1

    while left <= right:
        m = (left + right) // 2
        while m > left and arr[m] is "":
            m -= 1

        if arr[m] == key:
            return m
        if arr[m] > key:
            right = m - 1
        else:
            left = m + 1

    return -1


tests = [
    "at",
    "ball",
    "bong",
    "dad"
]

for test in tests:
    print(f"{test}: {sparse_search(sparse_arr, test)}")
    print(f"{test}: {sparse_search_2(sparse_arr, test)}")
    print(f"{test}: {sparse_search_3(sparse_arr, test)}")