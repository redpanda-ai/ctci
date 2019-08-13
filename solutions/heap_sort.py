def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    #print(arr[:n], arr[n:], i, n)
    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # build max heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    #print(f"Heapified:\n{arr}")

    for j in range(n-1, 0, -1):
        # swap
        arr[j], arr[0] = arr[0], arr[j]

        # heapify root element
        heapify(arr, j, 0)


if __name__ == "__main__":
    test = [12, 11, 13, 5, 6, 7]
    print(f"Heapsort for:\n{test}")
    heap_sort(test)
    print(test)