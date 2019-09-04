from collections import Counter


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def paths_with_sum(root, paths=[], target=0, target_count=None):
    if root:
        if not target_count:
            target_count = Counter()
        my_paths = [root.data] + [root.data + val for val in paths]
        target_count[target] += sum([1 for val in my_paths if val == target])
        paths_with_sum(root.left, my_paths, target, target_count)
        paths_with_sum(root.right, my_paths, target, target_count)

    return target_count[target]


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
             *    * 
           3        5
          *  *    *   *
        -2    7  3     5
    """
    targets = [
        4, 7, 10, 1
    ]
    for target in targets:
        answer = paths_with_sum(a, target=target)
        print(f"There are {answer} paths with sum {target}")