def heapify(arr, e, l):
    # find largest among root and children
    left = 2 * l + 1
    right = 2 * l + 2

    largest = l
    for c in [left, right]:
        if c < e and arr[largest] < arr[c]:
            largest = c

    if largest is not l:
        arr[l], arr[largest] = arr[largest], arr[l]
        heapify(arr, e, largest)


def heap_sort(arr):
    n = len(arr)

    # build max heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for j in range(n - 1, 0, -1):
        # swap
        arr[j], arr[0] = arr[0], arr[j]

        # heapify root element
        heapify(arr, j, 0)


if __name__ == "__main__":
    tests = [
        [12, 11, 13, 5, 6, 7, -1, 9],
        [],
        [4, 3, 2, 1]
    ]
    for test in tests:
        print(f"Heapsort for:\n{test}")
        heap_sort(test)
        print(test)