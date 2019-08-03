from binarytree import Node

class Solution:

    def solver(self, sorted_array):
        if len(sorted_array) == 0:
            return None
        if len(sorted_array) == 1:
            return Node(sorted_array[0])
        if len(sorted_array) == 2:
            root = Node(sorted_array[1])
            root.left = Node(sorted_array[0])
            return root
        if len(sorted_array) == 3:
            root = Node(sorted_array[1])
            root.left = Node(sorted_array[0])
            root.right = Node(sorted_array[2])
            return root
        else:
            mid = len(sorted_array) // 2
            # root = Node(sorted_array[mid])
            my_root = sorted_array[mid]
            root = Node(my_root)
            left_tree = sorted_array[:mid]
            right_tree = sorted_array[mid+1:]
            root.left = self.solver(left_tree)
            root.right = self.solver(right_tree)
            #print(f"my_root: {my_root}, left_tree: {left_tree}, right_tree: {right_tree}")
            return root

s = Solution()


for r in range(0, 20):
    sorted_array = range(r)
    answer = s.solver(sorted_array)
    is_balanced = None
    if answer:
        is_balanced = answer.is_balanced

    print(f"The solution for {sorted_array} is {answer}, is_balanced = {is_balanced}")

