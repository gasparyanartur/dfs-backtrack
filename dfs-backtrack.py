def get_longest_path_length(
    node: any, graph: dict[any, list[any]], lengths: dict[any, int]
) -> int:
    """Get the length of the longest path from the given node to any other node without making a cycle.

    Args:
        node: The node to start from.
        graph: A mapping from a node to all the neighbours.
        lengths: Mapping of each node to the longest neighbour.

    Returns:
        int: The length of the longest path.
    """
    print(node)
    if node in lengths:
        return lengths[node]

    lengths[node] = 0  # Initialize value to avoid cyclic paths.

    if node not in graph:
        lengths[node] = 1
        return 1

    max_len = 0
    for nb in graph[node]:
        max_len = max(get_longest_path_length(nb, graph, lengths) + 1, max_len)

    lengths[node] = max_len
    return max_len


if __name__ == "__main__":
    graph = {"a": ["b", "c"], "b": ["c", "d"], "c": ["d"], "d": ["b"]}  # a -> 4, d -> 3
    lengths = {}
    get_longest_path_length("a", graph, lengths)
    print(lengths)
