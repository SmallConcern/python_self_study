from collections import deque

graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}}


def bfs(graph, start):
    visited, queue = set(), deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return visited


def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        vertex, path = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def dfs_r(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for vertex in graph[start] - visited:
        dfs_r(graph, vertex, visited)
    return visited


def dfs_path(graph, start, end):
    stack = [(start, [start])]
    while stack:
        vertex, path = stack.pop()
        for next in graph[vertex] - set(path):
            if next == end:
                return path + [next]
            else:
                stack.append((next, path + [next]))


print "DFS: {}".format(dfs(graph, 'A'))
print "DFS_R: {}".format(dfs_r(graph, 'A'))
print "DFS Paths A->F: {}".format(dfs_path(graph, 'A', 'F'))
print "BFS: {}".format(bfs(graph, 'A'))
print "BFS Paths A->F: {}".format(bfs_path(graph, 'A', 'F'))

