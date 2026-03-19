import heapq
import random

GRID_SIZE = 10

def create_grid(density):
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if random.random() < density:
                grid[i][j] = 1
    return grid

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    pq = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}

    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            break

        for d in directions:
            next_node = (current[0] + d[0], current[1] + d[1])

            if 0 <= next_node[0] < GRID_SIZE and 0 <= next_node[1] < GRID_SIZE:
                if grid[next_node[0]][next_node[1]] == 1:
                    continue

                new_cost = cost_so_far[current] + 1

                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + heuristic(goal, next_node)
                    heapq.heappush(pq, (priority, next_node))
                    came_from[next_node] = current

    if goal not in came_from:
        return None

    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from[node]
    path.reverse()

    return path


grid = create_grid(0.2)

start = (0, 0)
goal = (9, 9)

path = a_star(grid, start, goal)

if path:
    print("Path:", path)
    print("Path Length:", len(path))
else:
    print("No path possible")