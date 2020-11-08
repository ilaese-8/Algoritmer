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

    def is_connected(self, vertice_one, vertice_two):
        temp = self.graph[vertice_one]
        while temp:
            if temp.value == vertice_two:
                return True
            temp = temp.next
        return False

    def get_neighbours(self, vertice):
        neighbours = []
        temp = self.graph[vertice]
        while temp:
            values = (temp.value, temp.weight)
            neighbours.append(values)
            temp = temp.next
        return neighbours
    
    def print_graph(self):
        for i in range(self.vertices):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.value),
                      "( weight: {}".format(temp.weight),
                      ")", end="")
                temp = temp.next
            print(" \n")
