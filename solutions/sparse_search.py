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
# sparse_arr = ["", "", ""]
# sparse_arr = ["at", "ball", "bong", "dad"]


def sparse_search(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right and arr[left] is "":
        left += 1
    while left <= right and arr[right] is "":
        right -= 1

    while left <= right:
        m = (left + right) // 2
        while m > left and arr[m] is "":
            m -= 1

        if arr[m] is key:
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