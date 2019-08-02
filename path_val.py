class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def convert_path_to_string(p):
    result = "["
    for item in p:
        result += (f"{str(item)}, ")
    result = result[:-2] + "]"

    return result


def parse_paths(my_path):
    for i in range(len(my_path)):
        partial = my_path[i:]
        list_string = convert_path_to_string(partial)
        results[list_string] = sum(partial)



def path_val(node: Node, val=0, path=[]):
    if not node:
        return 0
    val += node.data
    my_path = path + [node.data]
    # parse_paths(my_path)

    path_val(node.left, val=val, path=my_path)
    path_val(node.right, val=val, path=my_path)

    if not node.left and not node.right:
        while my_path:
            parse_paths(my_path)
            my_path = my_path[:-1]

results = {}

a = Node(3)
a.left = Node(5)
a.right = Node(-1)
a.left.left = Node(6)
a.left.right = Node(7)
a.right.left = Node(3)
a.right.right = Node(2)
a.right.right.left = Node(1)

path_val(a)

for path in sorted(results.keys()):
    print(f"Path: {path}, val: {results[path]}")
