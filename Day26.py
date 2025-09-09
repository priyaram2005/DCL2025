def detect_cycle(V, edges):
    graph = [[] for _ in range(V)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * V

    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for i in range(V):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False


print("Input: V = 5, Edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]")
print("Output:", detect_cycle(5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]))

print("\nInput: V = 3, Edges = [[0, 1], [1, 2]]")
print("Output:", detect_cycle(3, [[0, 1], [1, 2]]))

print("\nInput: V = 4, Edges = [[0, 1], [1, 2], [2, 0]]")
print("Output:", detect_cycle(4, [[0, 1], [1, 2], [2, 0]]))
