# Contribution Log

**Student:** Samruddhi Uddhavrao Patil  
**PRN:** 25UAM064  
**SLE:** 2 — BFS vs DFS Maze Pathfinding

| Stage | Work Completed | Result |
|---|---|---|
| 1 | Defined grid-maze problem and 4-direction movement | Maze model finalized |
| 2 | Implemented BFS using a queue | Shortest-path solver completed |
| 3 | Implemented depth-limited DFS | DFS solver completed |
| 4 | Added node-expansion counting and timing | Fair comparison metrics added |
| 5 | Added sampling profiler inspired by py-spy | Profiling workflow prepared |
| 6 | Compared best, average and worst cases | Results documented |
| 7 | Added graph/flame-graph representation | `graph.svg` added |
| 8 | Prepared README and conclusion | Repository documentation completed |

## Final Findings

- BFS always returned the shortest path in the tested mazes.
- DFS was faster and expanded fewer nodes in the tested corridor-like mazes.
- DFS did not guarantee a shortest path and produced a much longer path in the worst case.
- The profiling results showed most sampled execution time inside the search functions and `get_neighbors()`.

## AI Assistance

AI assistance was used for parts of the maze generation, BFS/DFS solver code, profiling driver, figure preparation and report formatting. The selected maze sizes, experiment execution, result checking and final interpretation were reviewed for the SLE-2 work.
