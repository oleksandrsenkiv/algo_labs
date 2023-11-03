from collections import deque

graph = {}
with open("input.txt", 'r') as file:
    for line in file:
        parts = line.strip().split(':')
        vertex = int(parts[0])
        neighbors = [int(n) for n in parts[1].split()]
        graph[vertex] = neighbors


def find_root_vertex(graph):
    vertices = set(graph.keys())
    num_vertices = len(vertices)
    for start_vertex in graph:
        visited = set()
        queue = deque([start_vertex])
        visited_idx = 0
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                visited_idx += 1
                if visited_idx == num_vertices:
                    return start_vertex
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
    return -1


result1 = find_root_vertex(graph)

with open("output.txt", 'w') as output_file:
    output_file.write(str(result1))
