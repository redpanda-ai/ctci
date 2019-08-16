class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def get_preorder_string(root):
    if not root:
        return 'X'
    return str(root.data) + get_preorder_string(root.left) + get_preorder_string(root.right)



a = Node(5)
b = Node(2)
c = Node(8)
d = Node(1)
e = Node(4)
f = Node(7)

a.left = b
a.right = c
b. left = d
b.right = e
c.left = f

g = Node(5)
h = Node(2)
g.left = h


a_string = get_preorder_string(a)
print(a_string)
c_string = get_preorder_string(c)
print(c_string)
g_string = get_preorder_string(g)
print(g_string)

tests = [
    [a, c],
    [c, a],
    [a, g]
]


for t1, t2 in tests:
    s1 = get_preorder_string(t1)
    s2 = get_preorder_string(t2)
    print(f"{s1} contains {s2}: {s1.__contains__(s2)}")


