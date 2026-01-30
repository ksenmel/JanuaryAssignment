def has_cycle(graph: dict[int, list[int]]) -> bool:
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
