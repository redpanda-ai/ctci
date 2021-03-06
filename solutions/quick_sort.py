def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == "__main__":
    tests =[
        [10, 9, 7, 8, 8, 9, 1, 5],
        [],
        [1],
        [2, 1],
        [1, 2, 3, 4, 5, 7, 7, 7, 6, 7, 8, 9]
    ]
    for test in tests:
        n = len(test)
        print(test)
        quick_sort(test, 0, n-1)
        print(test)
