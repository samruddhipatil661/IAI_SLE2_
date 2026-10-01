# SLE-2: BFS vs DFS Maze Pathfinding

**Course:** 02AML204 — Introduction to Artificial Intelligence  
**PRN:** 25UAM064  
**Name:** Samruddhi Uddhavrao Patil  
**Division:** A

## Objective

Compare **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** for solving a grid maze using 4-directional movement. The comparison uses execution time, nodes expanded, and solution path length.

## Repository Structure

```text
IAI_SLE2_/
├── README.md
├── main.py
├── bfs.py
├── dfs.py
├── sampling_profiler.py
├── CONTRIBUTION_LOG.md
└── graph.svg
```

## Algorithms

### BFS
- Uses a queue (FIFO).
- Explores nodes level by level.
- Complete and optimal for an unweighted grid.
- Returns the shortest path when one exists.

### DFS
- Uses a stack (LIFO).
- Follows one branch deeply before backtracking.
- Uses a depth limit of 200 in this project.
- Does not guarantee the shortest path.

## Maze Model

- Grid-based maze.
- `0` = open cell.
- `1` = wall.
- Movement is allowed up, down, left, and right.
- A start cell and goal cell are defined in `main.py`.

## Profiling

The report used an in-process sampling profiler based on periodic call-stack snapshots because `py-spy` was unavailable on the offline machine. The script follows the same profiling idea as py-spy.

If `py-spy` is installed, an equivalent command is:

```bash
py-spy record -o graph.svg --rate 100 -- python main.py
```

The included `sampling_profiler.py` can be used without external installation:

```bash
python sampling_profiler.py
```

## Report Results

| Metric | BFS | DFS |
|---|---:|---:|
| Best-case time | 0.0824 ms | 0.0512 ms |
| Average-case time | 0.4526 ms | 0.3605 ms |
| Worst-case time | 1.6566 ms | 0.9239 ms |
| Average nodes expanded | 480 | 270 |
| Optimal path | Yes | No |

DFS was faster on the tested corridor-like mazes, while BFS consistently produced the shortest path. The worst-case test produced a path of **78 moves with BFS** and **194 moves with DFS**.

## Complexity

- **BFS:** `O(b^d)` time and space in the standard search formulation.
- **DFS:** `O(b^m)` time with depth limit `m = 200`, with space proportional to the depth/search stack.

Here, `b` is the branching factor, `d` is the shallowest solution depth, and `m` is the depth limit.

## Run

```bash
python main.py
```

The program prints the maze, BFS result, DFS result, path lengths, and nodes expanded.

## Conclusion

**BFS is safe when the shortest path matters; DFS can be faster but may return a much longer path.**

## AI Contribution

AI assistance was used for parts of the maze generation, BFS/DFS implementation, profiling driver, chart/figure preparation, and report formatting. The maze sizes, experiments, result checking, and final analysis were selected and verified for the SLE-2 work.
