from collections import deque


def get_neighbors(maze, node):
    """Return valid 4-directional open-cell neighbours."""
    rows, cols = len(maze), len(maze[0])
    r, c = node
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
            neighbors.append((nr, nc))
    return neighbors


def bfs(maze, start, goal):
    """Breadth-First Search. Returns path, path length and nodes expanded."""
    queue = deque([start])
    parent = {start: None}
    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current == goal:
            return reconstruct_path(parent, goal), nodes_expanded

        for neighbor in get_neighbors(maze, current):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    return [], nodes_expanded


def reconstruct_path(parent, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path
