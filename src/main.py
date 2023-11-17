from collections import deque


def find_way_to_transport_gas(cities, warehouses, pipelines):
    graph = {}
    for city in cities + warehouses:
        graph[city] = []
    for pipeline in pipelines:
        graph[pipeline[0]].append(pipeline[1])
    result = []
    for warehouse in warehouses:
        visited = set()
        queue = deque([warehouse])
        current_cities = cities.copy()
        current_cities.insert(0, warehouse)
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                current_cities.remove(vertex)
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        if current_cities:
            result.append([warehouse, current_cities])
    return result
