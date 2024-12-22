# Определение класса Graph
class Graph:
	# Метод для добавления вершины
	def add_vertex(self,vertex):
		# Проверка, существует ли уже эта вершина в adj_list
		if vertex not in self.adj_list:
		# Если нет, создаем новый список для этой вершины
		self.adj_list[vertex]=[]

	# Метод для добавления ребра
	def add_edge(self,v1,v2):
		# Проверка, существуют ли обе вершины в adj_list
		if v1 in self.adj_list and v2 in self.adj_list:
			# Добавление v2 в список смежных вершин v1
			self.adj_list[v1].append(v2)
			# Добавление v1 в список смежных вершин v2
			self.adj_list[v2].append(v1)

	# Метод для вывода графа
	def display_graph(self):
		# Сортировка ключей словаря adj_list
		for vertex in sorted(self.adj_list.keys()):
			# Вывод каждой вершины и ее списка смежных вершин
			print(vertex,"->",self.adj_list[vertex])

# Создание экземпляра графа
graph=Graph()

# Добавление вершин
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')

# Добавление ребер
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'A')

# Вывод графа
print("Граф:")
graph.display_graph()