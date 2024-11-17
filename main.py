import numpy as np
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.adj_matrix = np.zeros((vertices, vertices), dtype=int)
        self.inc_matrix = None
        self.edge_list = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.adj_matrix[u][v] = 1
        self.edge_list.append((u, v))

    def create_inc_matrix(self):
        edges = self.edge_list
        self.inc_matrix = np.zeros((self.V, len(edges)), dtype=int)
        for idx, (u, v) in enumerate(edges):
            self.inc_matrix[u][idx] = 1
            self.inc_matrix[v][idx] = 1

    def print_adj_list(self):
        for vertex in range(self.V):
            print(f"Vertex {vertex}:", end="")
            for neighbour in self.graph[vertex]:
                print(f" -> {neighbour}", end="")
            print()

    def print_adj_matrix(self):
        print("Adjacency Matrix:")
        print(self.adj_matrix)

    def print_inc_matrix(self):
        print("Incidence Matrix:")
        print(self.inc_matrix)

    def print_edge_list(self):
        print("Edge List:")
        for edge in self.edge_list:
            print(f"{edge[0]} -> {edge[1]}")

# Пример использования (Полный граф)
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

g.create_inc_matrix()

g.print_adj_list()
g.print_adj_matrix()
g.print_inc_matrix()
g.print_edge_list()

# Пример использования (Разреженный граф)
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)

g.create_inc_matrix()

g.print_adj_list()
g.print_adj_matrix()
g.print_inc_matrix()
g.print_edge_list()

# Пример использования (Ориентированный граф)
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 0)

g.create_inc_matrix()

g.print_adj_list()
g.print_adj_matrix()
g.print_inc_matrix()
g.print_edge_list()
