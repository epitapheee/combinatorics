from collections import deque

def bfs(graph, root):
	visited = set()
	queue = deque([root])

	while queue:
		vertex = queue.popleft()
		print(vertex, end=" ")

		for neighbour in graph[vertex]:
			if neighbour not in visited:
				visited.add(neighbour)
				queue.append(neighbour)

graph = {
	'A': ['B', 'C'],
	'B': ['D', 'E'],
	'C': ['F'],
	'D': [],
	'E': ['F'],
	'F': []
}

bfs(graph, 'A')