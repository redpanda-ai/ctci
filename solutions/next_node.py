class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self._parent = None
        self._left = left
        self._right = right

    def __repr__(self):
        return f"{self.data}"

    def left(self, other):
        self._left = other
        other._parent = self

    def right(self, other):
        self._right = other
        other._parent = self

    def get_right(self):
        return self._right

    def get_left(self):
        return self._left

    def get_parent(self):
        return self._parent

    def is_right_child(self):
        if self.get_parent():
            return self.get_parent().get_right() == self
        return False

    def is_left_child(self):
        if self.get_parent():
            return self.get_parent().get_left() == self
        return False

    def is_tree_root(self):
        if self.get_parent() is None:
            return True
        return False


def in_order_walk(tree, start):
    if start:
        x = in_order_walk(tree, start.get_left())
        if x:
            return x
        y = start.data
        if y:
            return y
        z = in_order_walk(tree, start.get_right())
        if z:
            return z
        return None


def in_order_traversal(start):
    if start:
        in_order_traversal(start.get_left())
        print(start.data)
        in_order_traversal(start.get_right())


def next_node(tree, node: Node):
    if node.is_tree_root():
        print("Root node processing")
        x = node.get_right()
        if x:
            while x.get_left():
                x = x.get_left()
            return x
        return None

    if node.is_right_child():
        print("Right child processing")
        x = node.get_right()
        if x:
            while x.get_left():
                x = x.get_left()
            return x
        print("right no right")
        z = node.get_parent()
        if z.is_left_child():
            zz = z.get_parent()
            if zz.is_left_child():
                return zz
            while z.is_left_child():
                z = z.get_parent()
            return z
        if z.is_right_child():
            while z.is_right_child():
                z = z.get_parent()
        if not z.is_tree_root():
            return z
        return None

    if node.is_left_child():
        print("Left child processing")
        x = node.get_right()
        if x:
            while x.get_left():
                x = x.get_left()
            return x
        z = node.get_parent()
        if z:
            while z.is_left_child():
                z = z.get_parent()
        if not z.is_tree_root():
            return z
        return None




a = Node('a')
b = Node('b')
c = Node("c")
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

h = Node('h')

a.left(b)
a.right(c)
b.left(d)
b.right(e)
c.left(f)
c.right(g)
d.right(h)

tests = [
    a,
    b,
    c,
    d,
    e,
    f,
    g,
    h
]

in_order_traversal(a)
for test in tests:
    print(f"{test.data} -> {next_node(a, test)}")



