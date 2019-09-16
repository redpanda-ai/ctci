def search_rotated_array(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        m = (low + high) // 2

        if arr[m] == target:
            return m
        if arr[low] < arr[m]:
            if arr[low] <= target < arr[m]:
                high = m - 1
            else:
                low = m + 1
        else:
            if arr[m] < target <= arr[high]:
                low = m + 1
            else:
                high = m - 1

    return -1

if __name__ == "__main__":
    test = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    targets = test + [21]
    for target in targets:
        print(f"{target} is in index {search_rotated_array(test, target)} of {test}")