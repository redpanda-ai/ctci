from binarytree import Node


def minimal_tree(arr, low, high):
    if low < high:
        m = (low + high) // 2
        return Node(arr[m], left=minimal_tree(arr, low, m), right=minimal_tree(arr, m + 1, high))


test_arrays = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4],
    [0, 2, 4, 6, 7, 9]
]
for array in test_arrays:
    l, h = 0, len(array)
    x = minimal_tree(array, l, h)
    print(x, x.is_balanced)
