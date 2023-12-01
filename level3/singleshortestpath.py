import heapq

def dijkstra(graph, start):
    q, d = [(0, start)], {start: 0}
    while q:
        dist, node = heapq.heappop(q)
        for neighbor, weight in enumerate(graph[node]):
            if weight and dist + weight < d.get(neighbor, float('inf')):
                heapq.heappush(q, (dist + weight, neighbor))
                d[neighbor] = dist + weight
    return d

# Example usage (replace `graph` and `start_node`):
graph = [
    [0, 4, 0, 0, 0],
    [4, 0, 8, 0, 0],
    [0, 8, 0, 7, 0],
    [0, 0, 7, 0, 9],
    [0, 0, 0, 9, 0]
]
start_node = 0
shortest_distances = dijkstra(graph, start_node)
print("Shortest distances:", shortest_distances)
