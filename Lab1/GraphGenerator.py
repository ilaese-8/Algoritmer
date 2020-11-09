import random
from AdjacencyListGraph import*
#from AdjacencyMatrixGraph import*

class GraphGenerator:

    # Generates a connected graph with a chosen connection density
    def generate_graph(self, size, connection_density):
        graph = Graph(size)
        for density in range(connection_density):
            graph = self.connect_graph(size, graph)
        return graph

    # Adds as many non-pointed edges as the amount of vertices in the graph
    def connect_graph(self, size, graph):
        vertices = self.get_shuffled_array(size)
        for i in range(1, size):
            weight = random.randint(1, 10)
            graph.add_edge(vertices[i - 1], vertices[i], weight)
        return graph

    # Generates a shuffled array using the Fisher-Yates shuffling method
    def get_shuffled_array(self, size):
        arr = []
        for i in range(size):
            arr.append(i)
        for j in range(size - 1, 0, - 1): 
            k = random.randint(0, i)
            arr[j],arr[k] = arr[k],arr[j]
        return arr

    # Generates and returns graphs
    def get_graphs(self, amount, size, connection_density):
        if connection_density < 1 or size < 1 or amount < 1:
            return
        graphs = []
        for graph in range(amount):
            new_graph = self.generate_graph(size, connection_density)
            graphs.append(new_graph)
        return graphs
        
def main():
    
    g = GraphGenerator()
    graphs = g.get_graphs(1, 7, 1)
    for graph in graphs:
        graph.traverse()

if __name__ == "__main__":
    main()
