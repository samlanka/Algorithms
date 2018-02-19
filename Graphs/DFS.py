#Depth-first-search graph traversal
#Author: Sameera Lanka

def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for neighbour in graph[node]:
                stack.append(neighbour)
    return visited
