classGraph:
	# Метод для добавления ребра между двумя вершинами
	def add_edge(self,vertex1,vertex2):
		# Добавляем кортеж (вершина1,вершина2) в список ребер
		self.edges.append((vertex1,vertex2))
	# Метод для вывода списка всех ребер графа
	def print_edges(self):
		print("Списокрёбер:")
		# Проходим по всем ребрам в списке self.edges
		for edge in self.edges:
			# Выводим информацию о каждом ребре в формате "вершина1->вершина2
			print(f"{edge[0]}->{edge[1]}")

	# Создаем экземпляр класса Graph
	graph=Graph()

	# Добавляем ребра в граф
	# Каждая строка добавляет одно ребро между двумя вершинами
	graph.add_edge(0,1)
	graph.add_edge(0,2)
	graph.add_edge(1,2)
	graph.add_edge(2,3)
	graph.add_edge(3,4)

	# Выводим список всех ребер графа
	graph.print_edges()