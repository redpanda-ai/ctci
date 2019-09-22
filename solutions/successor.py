class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def set_left(self, other):
        self.left = other
        other.parent = self

    def set_right(self, other):
        self.right = other
        other.parent = self


def leftmost_child(node: Node):
    while node.left:
        node = node.left

    return node


def successor(node: Node):
    if node is None:
        return

    if node.right:
        return leftmost_child(node.right)

    q = node
    x = q.parent
    while x and x.left is not q:
        q = x
        x = x.parent
    return x


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")

    a.set_left(b)
    a.set_right(c)

    b.set_left(d)
    b.set_right(e)

    c.set_left(f)
    c.set_right(g)

    """           
                    a
                   *  *            
                  *    *
                 *      * 
                b        c
               * *      * *
              *   *    *   *
             d     e  f     g
    """

    r = leftmost_child(a)
    while r:
        print(r.value)
        r = successor(r)

