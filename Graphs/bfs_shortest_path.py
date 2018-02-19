#Shortest path between 2 nodes in a graph via breadth first search
#Author: Sameera Lanka
from collections import deque

def bfs_shortest_path(graph, start, end):
    if start == end:
        return "Start and end are same node"
    else:
        visited, queue = [], deque([[start]])
        while queue:
            shortestPath = queue.popleft()
            node = shortestPath[-1]
            if node not in visited:
                visited.append(node)
                for neighbour in graph[node]:
                    newpath = shortestPath[:].append(neighbour)
                    queue.append(newpath)

                    if neighbour == end:
                        return newpath
        return "Path does not exist"
