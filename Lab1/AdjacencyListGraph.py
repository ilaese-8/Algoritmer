class Node:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.next = None


class Graph:
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices

    def add_edge(self, source, destination, weight):
        if weight < 1:
            return
        node = Node(destination, weight)
        node.next = self.graph[source]
        self.graph[source] = node
        node = Node(source, weight)
        node.next = self.graph[destination]
        self.graph[destination] = node

    def get_neighbours(self, vertice):
        neighbours = []
        for index in range(self.size):
            value = self.matrix[vertice][index]
            if value > 0:
                neighbours.append((index, value))
        return neighbours

    def traverse(self):
        visited = [False] * self.vertices
        counter = 0
        for i in range(self.vertices):
            vertice = self.graph[i]
            while vertice != None:
                val = vertice.value
                if not visited[val]:
                    print("Visiting vertice: ", val)
                    visited[val] = True
                    counter += 1
                vertice = vertice.next
        print(" \nNodes visited: ", counter)

                    
    
