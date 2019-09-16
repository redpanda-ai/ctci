from binarytree import Node


def get_balanced_tree(arr):
    if len(arr) == 0:
        return
    m = len(arr) // 2
    left, right = arr[:m], arr[m + 1:]
    return Node(arr[m], left=get_balanced_tree(left), right=get_balanced_tree(right))


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
    # x = get_balanced_tree(array)
    low, high = 0, len(array)
    x = minimal_tree(array, low, high)
    print(x, x.is_balanced)
