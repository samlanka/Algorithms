#Recursive implementation of depth-first search
#Author: Sameera Lanka

def dfs_recursive(graph, start, visited=[]):
    visited.append(start)
    for neighbour in graph[start]:
        if neighbour not in visited:
            visited = dfs_recursive(graph, neighbour, visited)
    return visited
