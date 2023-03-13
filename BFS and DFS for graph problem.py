class graph_solutions():
    def __init__(self) -> None:
        pass

    def dfs(graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start)
        for neighbor in graph[start] - visited:
            dfs(graph, neighbor, visited)
        return visited

    def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)