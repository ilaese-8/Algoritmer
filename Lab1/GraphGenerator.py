import random
from AdjacencyListGraph import*
from AdjacencyMatrixGraph import*

class GraphGenerator:

    # Generates a list graph
    def generate_list_graph(self, size):
        list_graph = ListGraph(size)
        vertex_arr = self.get_shuffled_array(size)
        for i in range(1, size):
            weight = random.randint(1, 10)
            list_graph.add_edge(vertex_arr[i - 1], vertex_arr[i], weight)
        return list_graph
        

    # Shuffles an array using the Fisher-Yates algorithm    
    def get_shuffled_array(self, size):
        arr = self.generate_array(size)
        for i in range(size-1,0,-1): 
            j = random.randint(0, i)
            arr[i],arr[j] = arr[j],arr[i]
        return arr 

    # Generates a vertex array with a given size
    def generate_array(self, size):
        vertex_numbers = []
        for i in range(size):
            vertex_numbers.append(i)
        return vertex_numbers

    # Generates a matrix graph
    def generate_matrix_graph(self, size):
        matrix_graph = MatrixGraph(size)
        vertex_arr = self.get_shuffled_array(size)
        for i in range(1, size):
            weight = random.randint(1, 10)
            matrix_graph.add_edge(vertex_arr[i - 1], vertex_arr[i], weight)
        return matrix_graph

    # Gets the requested amount of list graphs
    def get_list_graphs(self, amount, size):
        graphs = []
        for x in range(amount):
            list_graph = self.generate_list_graph(size)
            graphs.append(list_graph)
        return graphs

    # Gets the requested amount of matrix graphs
    def get_matrix_graphs(self, amount, size):
        graphs = []
        for x in range(amount):
            matrix_graph = self.generate_matrix_graph(size)
            graphs.append(matrix_graph)
        return graphs

def main():
    g = GraphGenerator()

    matrix_graphs = g.get_matrix_graphs(2, 10)
    for graph in matrix_graphs:
        graph.print_matrix()
        print('\n')

    list_graphs = g.get_list_graphs(2, 10)
    for graph in list_graphs:
        graph.print_graph()
        print('\n')

if __name__ == "__main__":
    main()

