def solve(arr, target):
    # binary search
    l, r = 0, len(arr) - 1

    while l < r:
        print(f"l: {l}, r: {r}")
        m = (l + r) // 2
        if arr[m] == target:
            return m
        elif arr[l] < arr[m]:  # left half sorted
            if arr[l] < target:
                r = m - 1
            else:
                l = m + 1
        else:  # right half sorted
            if target < arr[r]:
                l = m + 1
            else:
                r = m - 1

    if arr[l] == target:
        return l
    return -1

my_list = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]

print(solve(my_list, 5))
print(solve(my_list, 32))
print(solve(my_list, 19))