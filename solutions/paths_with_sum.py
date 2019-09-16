from collections import Counter


class Node:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


def paths_with_sum(root, target=0, counter=None):
    if root:
        if counter is None:
            counter = Counter()
        path_val = root.data
        if path_val is target:
            counter[target] += 1
        r = root
        while r.parent:
            path_val += r.parent.data
            r = r.parent
            if path_val is target:
                counter[target] += 1
        for child in [root.left, root.right]:
            paths_with_sum(child, target, counter)

    return counter[target]


if __name__ == "__main__":
    a = Node(4)
    a.left = Node(3)
    a.left.parent = a
    a.right = Node(5)
    a.right.parent = a
    a.left.left = Node(-2)
    a.left.left.parent = a.left
    a.left.right = Node(7)
    a.left.right.parent = a.left
    a.right.left = Node(3)
    a.right.left.parent = a.right
    a.right.right = Node(5)
    a.right.right.parent = a.right

    """
                 4
               *   * 
            3          5
           *   *      *   *
        -2      7   3       5
    """
    targets = [
        4, 7, 10, 1, 0, 5
    ]
    for target in targets:
        answer = paths_with_sum(a, target=target)
        print(f"There are {answer} paths with sum {target}")