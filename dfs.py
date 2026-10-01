from bfs import get_neighbors, reconstruct_path


def dfs(maze, start, goal, depth_limit=200):
    """Depth-Limited DFS. Returns path, path length and nodes expanded."""
    stack = [(start, 0)]
    parent = {start: None}
    depth = {start: 0}
    nodes_expanded = 0

    while stack:
        current, current_depth = stack.pop()
        nodes_expanded += 1

        if current == goal:
            return reconstruct_path(parent, goal), nodes_expanded

        if current_depth >= depth_limit:
            continue

        neighbors = get_neighbors(maze, current)
        for neighbor in reversed(neighbors):
            if neighbor not in depth:
                depth[neighbor] = current_depth + 1
                parent[neighbor] = current
                stack.append((neighbor, current_depth + 1))

    return [], nodes_expanded
