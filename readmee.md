README – Pathfinding Algorithms (AI Assignment)

Preethi Uyyuru - Se24ucse047

Overview:
This project implements different search algorithms to find optimal paths in various environments. It focuses on handling both static and dynamic conditions using Artificial Intelligence techniques.


1. Dijkstra’s Algorithm (Uniform Cost Search)

- Used to find the shortest path between cities with different distances.
- It expands the node with the minimum total cost.
- Implemented using a priority queue.

Features:
- Works on weighted graphs
- Finds shortest distance from source to all nodes
- Can also track the actual path

2. A* Algorithm (Static Obstacles)

- Used for grid-based navigation where obstacles are known.
- Uses both cost and heuristic to find the optimal path.

Formula:
f(n) = g(n) + h(n)

Where:
g(n) = cost from start
h(n) = estimated cost to goal

Heuristic Used:
- Manhattan Distance

Features:
- Faster than Dijkstra
- Avoids obstacles efficiently
- Suitable for robotics and navigation systems


3. Dynamic Environment (UGV Navigation)

- Simulates a robot moving in a changing environment.
- Obstacles can appear randomly during movement.

Approach:
- Uses A* algorithm repeatedly (replanning)
- Updates path when new obstacles are detected

Features:
- Handles dynamic obstacles
- Demonstrates real-world navigation


Files present:

python3 dijkstra.py
python3 ugv_static.py
python3 ugv_dynamic.py


Observations:

- Dijkstra guarantees shortest path but is slower
- A* is faster due to heuristic guidance
- Dynamic environments require continuous replanning


Conclusion:

This project shows how different algorithms are used based on the situation. Dijkstra is useful for weighted graphs, A* is better for grid navigation, and dynamic environments require continuous updates.
