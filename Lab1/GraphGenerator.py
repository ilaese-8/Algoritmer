import random
from AdjacencyListGraph import*
#from AdjacencyMatrixGraph import*

class GraphGenerator:

    def generate_graph(self, size):
        graph = Graph(size)
        connected_graph = self.connect_graph(size, graph)
        return connected_graph

    def connect_graph(self, size, graph):
        vertice_arr = self.get_shuffled_array(size)
        for i in range(1, len(vertice_arr)):
            weight = random.randint(1, 10)
            graph.add_edge(vertice_arr[i - 1], vertice_arr[i], weight)
        return graph

    def get_shuffled_array(self, size):
        arr = []
        for i in range(size):
            arr.append(i)
        for j in range(size-1,0,-1): 
            k = random.randint(0, i)
            arr[j],arr[k] = arr[k],arr[j]
        return arr

    def get_graphs(self, amount, size):
        graphs = []
        for graph in range(amount):
            new_graph = self.generate_graph(size)
            graphs.append(new_graph)
        return graphs
        
def main():
    
    g = GraphGenerator()
    graphs = g.get_graphs(1, 10)
    for graph in graphs:
        graph.print_graph()
        print('\n')
        

if __name__ == "__main__":
    main()
