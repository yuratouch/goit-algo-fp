import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Створюємо піраміду і додаємо початкову вершину
    priority_queue = [(0, start)]
    while priority_queue:
        # Виймаємо вершину з мінімальною відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Якщо знайдена відстань більше за поточну, пропускаємо цю вершину
        if current_distance > distances[current_vertex]:
            continue
        
        # Оновлюємо відстані до сусідів поточної вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Якщо знайдена нова коротша відстань, оновлюємо її
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def main():

    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    start_vertex = 'A'
    shortest_paths = dijkstra(graph, start_vertex)
    
    print(f"Найкоротші шляхи від вершини {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"Відстань до {vertex}: {distance}")

if __name__ == "__main__":
    main()
