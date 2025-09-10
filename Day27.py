from collections import deque, defaultdict

def shortest_path(V, edges, start, end):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    if start == end:
        return 0

    visited = [False] * V
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        node, dist = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if neighbor == end:
                    return dist + 1
                visited[neighbor] = True
                queue.append((neighbor, dist + 1))

    return -1


# Test Case 1
V1 = 5
edges1 = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
start1 = 0
end1 = 4
print("Shortest path length:", shortest_path(V1, edges1, start1, end1))

# Test Case 2
V2 = 3
edges2 = [[0, 1], [1, 2]]
start2 = 0
end2 = 2
print("Shortest path length:", shortest_path(V2, edges2, start2, end2))

# Test Case 3
V3 = 4
edges3 = [[0, 1], [1, 2]]
start3 = 2
end3 = 3
print("Shortest path length:", shortest_path(V3, edges3, start3, end3))
