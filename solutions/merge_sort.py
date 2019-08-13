def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l_arr = arr[:mid]
        r_arr = arr[mid:]

        merge_sort(l_arr)
        merge_sort(r_arr)

        i = j = k = 0

        while i < len(l_arr) and j < len(r_arr):
            if l_arr[i] < r_arr[j]:
                arr[k] = l_arr[i]
                i += 1
            else:
                arr[k] = r_arr[i]
                j += 1
            k += 1

        while i < len(l_arr):
            arr[k] = l_arr[i]
            i += 1
            k += 1

        while j < len(r_arr):
            arr[k] = r_arr[j]
            j += 1
            k += 1


if __name__ == "__main__":
    tests = [
        [2, 1, 3, 5, 4, 7]
    ]
    for test in tests:
        print(f"Input: {test}")
        merge_sort(test)
        print(f"Output: {test}")