from collections import defaultdict
import heapq


def get_smallest_spanning_edge(nodes_in: set, nodes_out: set, edge_dict: defaultdict) -> tuple:
    smallest_spanning_edge = (float("inf"), None, None)

    for tree_node in nodes_in:
        looking_for_edge = True
        while looking_for_edge:
            edge = node_1 = node_2 = None
            if edge_dict[tree_node]:
                edge = edge_dict[tree_node][0]
                _, node_1, node_2 = edge

            if edge is None:
                looking_for_edge = False
            elif node_1 in nodes_out or node_2 in nodes_out:
                smallest_spanning_edge = min(smallest_spanning_edge, edge)
                looking_for_edge = False
            else:
                heapq.heappop(edge_dict[tree_node])

    _, v1, v2 = smallest_spanning_edge
    nodes_in.add(v1)
    nodes_in.add(v2)
    nodes_out.discard(v1)
    nodes_out.discard(v2)

    return smallest_spanning_edge


def prim(my_edges: list) -> list:
    """"""
    edge_dict = defaultdict(list)
    # Transform the adjacency list into a dictionary, creating a min-heap of edges for each vertex
    for e in my_edges:
        cost, v1, v2 = e
        heapq.heappush(edge_dict[v1], e)
        heapq.heappush(edge_dict[v2], e)

    non_tree_nodes = set(edge_dict.keys())
    tree_nodes = set(non_tree_nodes.pop())
    tree_edges = list()

    # Systematically build a minimal spanning tree from the smallest (best) edge that will add a new node to
    # the tree
    while non_tree_nodes:
        smallest_spanning_edge = get_smallest_spanning_edge(tree_nodes, non_tree_nodes, edge_dict)
        tree_edges.append(smallest_spanning_edge)

    return tree_edges


if __name__ == "__main__":
    """This implementation uses an adjacency list with a tuple of (cost, vertex_1, and vertex_2) to represent
    each edge"""
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
        (2, "b", "g"),
        (9, "g", "h"),
        (3, "e", "h")
    ]

    mst = prim(edges)
    print(f"Minimal spanning tree of {edges}")
    total_cost = 0
    for my_edge in mst:
        edge_cost, _, _ = my_edge
        total_cost += edge_cost
        print(my_edge)
    print(f"Total cost: {total_cost}")
