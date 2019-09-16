from binarytree import Node, bst

class LNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        s = f"[{self.value}"
        r = self
        while r.next:
            r = r.next
            s += f" -> {r.value}"
        s += "]"
        return s


def list_of_depths(root: Node, list_starts=None, list_ends=None, depth=-0):
    if root:
        my_depth = depth + 1
        if not list_starts:
            list_starts = {}
        if not list_ends:
            list_ends = {}
        if my_depth not in list_starts:
            list_starts[my_depth] = list_ends[my_depth] = LNode(root.value)
        else:
            list_ends[my_depth].next = LNode(root.value)
            list_ends[my_depth] = list_ends[my_depth].next

        children = [root.left, root.right]
        for child in children:
            list_of_depths(child, list_starts=list_starts, list_ends=list_ends, depth=my_depth)

        return list_starts


if __name__ == "__main__":
    tree = bst(4)
    print(tree)
    answer = list_of_depths(tree)
    print(answer)
