"""SLE-2 main program: compare BFS and DFS on a grid maze."""

from time import perf_counter

from bfs import bfs
from dfs import dfs


# 0 = open cell, 1 = wall
MAZE = [
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 0],
]

START = (0, 0)
GOAL = (7, 7)


def print_maze(maze, path=None):
    path = set(path or [])
    for r, row in enumerate(maze):
        line = []
        for c, cell in enumerate(row):
            pos = (r, c)
            if pos == START:
                line.append("S")
            elif pos == GOAL:
                line.append("G")
            elif pos in path:
                line.append("*")
            elif cell == 1:
                line.append("#")
            else:
                line.append(".")
        print(" ".join(line))


def run_algorithm(name, solver):
    start_time = perf_counter()
    path, nodes_expanded = solver(MAZE, START, GOAL)
    elapsed_ms = (perf_counter() - start_time) * 1000

    print(f"\n{name}")
    print("-" * 30)
    print(f"Time          : {elapsed_ms:.4f} ms")
    print(f"Nodes expanded: {nodes_expanded}")
    print(f"Path length   : {len(path) - 1 if path else 'No path'}")
    print_maze(MAZE, path)
    return path, elapsed_ms, nodes_expanded


def main():
    print("SLE-2: BFS vs DFS Maze Pathfinding")
    print("==================================")
    print(f"Start: {START} | Goal: {GOAL}")

    bfs_path, bfs_time, bfs_nodes = run_algorithm("BFS", bfs)
    dfs_path, dfs_time, dfs_nodes = run_algorithm(
        "DFS (depth limit = 200)",
        lambda maze, start, goal: dfs(maze, start, goal, depth_limit=200),
    )

    print("\nComparison")
    print("----------")
    print(f"BFS: {bfs_time:.4f} ms, {bfs_nodes} nodes, path = {len(bfs_path) - 1}")
    print(f"DFS: {dfs_time:.4f} ms, {dfs_nodes} nodes, path = {len(dfs_path) - 1}")
    print("BFS guarantees the shortest path in this unweighted maze.")
    print("DFS may be faster, but its returned path is not guaranteed to be shortest.")


if __name__ == "__main__":
    main()
