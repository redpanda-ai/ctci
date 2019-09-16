from collections import deque


class Node:
    def __init__(self, val, adj=None):
        self.val = val
        if not adj:
            self.adj = []
        else:
            self.adj = adj

    def __repr__(self):
        return f"val: {self.val}, adj: {self.adj}"


def route_between_nodes(node_a, node_b, graph):
    exploring = deque([node_a])
    visited = set()
    while exploring:
        print(f"Exploring: {exploring}, visited: {visited}")
        current = exploring.popleft()
        if current == node_b:
            return True
        if current not in visited:
            visited.add(current)
            exploring.extend(graph[current].adj)

    return False



if __name__ == "__main__":
    g = {}
    g["a"] = Node("a", ["b", "c"])
    g["b"] = Node("b", ["a", "d"])
    g["c"] = Node("c", ["b", "f"])
    g["d"] = Node("d")
    g["e"] = Node("e")
    g["f"] = Node("f", ["g"])
    g["g"] = Node("g")

    g["x"] = Node("x", ["y"])
    g["y"] = Node("y", ["z"])
    g["z"] = Node("z", ["x"])

    tests = [
        ["a", "a"],
        ["a", "b"],
        ["a", "c"],
        ["a", "d"],
        ["a", "e"],
        ["a", "f"],
        ["a", "g"],
        ["x", "z"],
        ["x", "a"]
    ]
    for a, b in tests:
        print(f"Route between {a} and {b}: {route_between_nodes(a, b, g)}")