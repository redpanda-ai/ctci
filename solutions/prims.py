from collections import defaultdict
import heapq


def get_best_edge(tree_nodes, non_tree_nodes, edge_dict):
    maybe = []
    for node in tree_nodes:
        maybe_found = False
        while not maybe_found:
            edge = None
            if edge_dict[node]:
                edge = edge_dict[node][0]

            if edge is None:
                maybe_found = True
            elif edge[1] in non_tree_nodes or edge[2] in non_tree_nodes:
                maybe_found = True
                heapq.heappush(maybe, edge)
            else:
                heapq.heappop(edge_dict[node])

    min_maybe = heapq.heappop(maybe)
    _, v1, v2 = min_maybe
    tree_nodes.add(v1)
    tree_nodes.add(v2)
    non_tree_nodes.discard(v1)
    non_tree_nodes.discard(v2)

    return min_maybe


def prim(my_edges: list):
    edge_dict = defaultdict(list)
    for e in my_edges:
        cost, v1, v2 = e
        heapq.heappush(edge_dict[v1], e)
        heapq.heappush(edge_dict[v2], e)

    non_tree_nodes = set(edge_dict.keys())
    tree_nodes = set(non_tree_nodes.pop())
    tree_edges = list()

    while non_tree_nodes:
        best_edge = get_best_edge(tree_nodes, non_tree_nodes, edge_dict)
        tree_edges.append(best_edge)

    return tree_edges


if __name__ == "__main__":
    edges = [
        (4, "a", "b"),
        (3, "a", "c"),
        (2, "a", "d"),
        (3, "b", "c"),
        (1, "b", "d"),
        (3, "c", "e"),
        (4, "d", "e"),
        (3, "e", "f"),
        (2, "c", "f"),
        (3, "c", "g"),
        (4, "d", "g"),
        (2, "b", "g")
    ]

    mst = prim(edges)
    print(f"Minimal spanning tree of {edges}")
    total_cost = 0
    for my_edge in mst:
        cost, _, _ = my_edge
        total_cost += cost
        print(my_edge)
    print(f"Total cost: {total_cost}")
