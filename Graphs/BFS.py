#Breadth-first search
#Author: Sameera Lanka
from collections import deque

def bfs(graph, start):
    visited, queue = [], deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbour in graph[node]:
                queue.append(neighbour)
    return visited
