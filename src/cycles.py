def has_cycle(graph: dict[int, list[int]]) -> bool:
    """
    Checks for a cycle in a directed graph using depth-first search (DFS).

    Args:
        graph: A directed graph represented as an adjacency dictionary,
        where keys are vertices and values are lists of adjacent vertices.
        Example: {0: [1, 2], 1: [2], 2: []}

    Returns:
        bool: True if the graph contains at least one cycle, False otherwise.

    Raises:
        TypeError: If graph is not a dictionary or if the adjacent list of vertices
        is not a list.
        ValueError: If an adjacent vertex is absent from the vertex set of a graph.
    """
    if not isinstance(graph, dict):
        raise TypeError("Graph must be a dictionary")

    for vertex, neighbors in graph.items():
        if not isinstance(neighbors, list):
            raise TypeError(f"Neighbors of vertex {vertex} must be a list")

        for neighbor in neighbors:
            if neighbor not in graph:
                raise ValueError(
                    f"Neighbor {neighbor} is not present in graph vertices"
                )

    in_progress = set[int]()
    visited = set[int]()

    for start_vertex in graph:
        if start_vertex in visited:
            continue

        stack = [start_vertex]
        in_progress.add(start_vertex)

        while stack:
            vertex = stack[-1]
            has_unvisited = False

            for neighbor in graph.get(vertex, []):
                if neighbor in in_progress:
                    return True

                if neighbor not in in_progress and neighbor not in visited:
                    in_progress.add(neighbor)
                    stack.append(neighbor)
                    has_unvisited = True
                    break

            if not has_unvisited:
                stack.pop()
                in_progress.remove(vertex)
                visited.add(vertex)

    return False
