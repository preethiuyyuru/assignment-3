import heapq

graph = {
    "Hyderabad": {"Bangalore": 570, "Chennai": 630},
    "Bangalore": {"Hyderabad": 570, "Mumbai": 980, "Chennai": 350},
    "Chennai": {"Hyderabad": 630, "Bangalore": 350, "Kolkata": 1670},
    "Mumbai": {"Bangalore": 980, "Delhi": 1400},
    "Delhi": {"Mumbai": 1400, "Kolkata": 1500},
    "Kolkata": {"Delhi": 1500, "Chennai": 1670}
}

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}

    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parent[neighbor] = current_node
                heapq.heappush(pq, (new_distance, neighbor))

    return distances, parent

def get_path(parent, city):
    path = []
    while city:
        path.append(city)
        city = parent[city]
    return path[::-1]


start_city = "Hyderabad"
distances, parent = dijkstra(graph, start_city)

print(f"\nShortest distances from {start_city}:\n")

for city in distances:
    path = get_path(parent, city)
    print(f"{city:10} → {distances[city]} km | Path: {' → '.join(path)}")