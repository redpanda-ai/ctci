class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        r = self
        result = ""
        while r:
            result += r.data + " -> "
            r = r.next

        return result


def delete_middle_node(root: Node, target: Node):
    runner = root
    trailer = None
    while runner.next:
        trailer = runner
        runner = runner.next
        if runner == target:
            trailer.next = runner.next


if __name__ == "__main__":
    root = Node(data='a')
    b = Node(data="b")
    c = Node(data="c")
    d = Node(data="d")
    e = Node(data="e")

    root.next = b
    b.next = c
    c.next = d
    d.next = e

    print(root)
    targets = [b, c, d]
    for target in targets:
        print(f"Deleting {target.data} from middle of : {root}")
        delete_middle_node(root, target)
        print(f"{root}")