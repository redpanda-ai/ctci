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

    non_tree_verts = set(edge_dict.keys())
    tree_verts = set(non_tree_verts.pop())
    tree_edges = list()

    while non_tree_verts:
        best_edge = get_best_edge(tree_verts, non_tree_verts, edge_dict)
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
        (4, "d", "e")
    ]

    mst = prim(edges)
    print(f"Minimal spanning tree of {edges}")
    for edge in mst:
        print(edge)