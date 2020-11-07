class MatrixGraph:

    def __init__(self, size):
        self.matrix = [[0 for i in range(size)] for j in range(size)] 

    def add_edge(self, vertice_one, vertice_two, weight):
        if weight < 1:
            return
        self.matrix[vertice_one][vertice_two] = weight
        self.matrix[vertice_two][vertice_one] = weight

    def is_connected(self, vertice_one, vertice_two):
        if self.matrix[vertice_one][vertice_two] > 0:
            return True
        return False

    def print_matrix(self):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in self.matrix]))