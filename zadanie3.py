import heapq

def dijkstra(graph, start):

    # Inicjalizacja odległości i kolejki priorytetowej
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Pomijamy przetworzone wierzchołki
        if current_distance > distances[current_node]:
            continue

        # Przeglądamy sąsiadów
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Aktualizacja dystansu, jeśli znaleziono krótszy
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 3},
    'D': {}
}

# Startujemy z wierzchołka 'A'
shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)
