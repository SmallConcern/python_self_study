

graph = {'A': ['B', 'C'],
		'B': ['D', 'C'],
		'C': ['D'],
		'D': ['E'],
		'E': ['F'],
		'F': ['A']}

def bfs(graph, start):
	path = []
	queue = [start]
	while queue:
		node = queue.pop(0)
		if node not in path:
			path = path + [node]
			queue = graph[node] + queue
	return path

def dfs(graph, start):
	path = []
	stack = [start]
	while stack:
		node = stack.pop(0)
		if node not in path:
			path = path + [node]
			stack = stack + graph[node]
	return path

def recursive_dfs(graph, start, path=[]):
	path = path + [start]
	for node in graph[start]:
		if not node in path:
			path = recursive_dfs(graph, node, path)
	return path

def find_path(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return path
	if not graph.has_key(start):
		return None
	for node in graph[start]:
		if node not in path:
			new_path = find_path(graph, node, end, path)
			if new_path:
				return new_path

def find_all_paths(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return [path]
	if not graph.has_key(start):
		return []
	paths = []
	for node in graph[start]:
		if node not in path:
			paths += find_all_paths(graph, node, end, path)
	return paths

def print_paths(paths):
	for path in paths:
		print "-->".join(path)

print dfs(graph, 'A')
print bfs(graph, 'A')
print recursive_dfs(graph, 'A')

