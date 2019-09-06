from collections import Counter


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def paths_with_sum(root, target=0, counter=Counter(), base=[]):
    if root:
        my_base = [root.data] + [root.data + val for val in base]
        counter[target] += len([val for val in my_base if val == target])
        paths_with_sum(root.left, target, counter, my_base)
        paths_with_sum(root.right, target, counter, my_base)

    return counter[target]


if __name__ == "__main__":
    a = Node(4)
    a.left = Node(3)
    a.right = Node(5)
    a.left.left = Node(-2)
    a.left.right = Node(7)
    a.right.left = Node(3)
    a.right.right = Node(5)

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