class Graph:

    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for i in range(size)] for j in range(size)] 

    def add_edge(self, vertice_one, vertice_two, weight):
        if weight < 1:
            return
        self.matrix[vertice_one][vertice_two] = weight
        self.matrix[vertice_two][vertice_one] = weight

    def get_neighbours(self, vertice):
        neighbours = []
        for index in range(self.size):
            value = self.matrix[vertice][index]
            if value > 0:
                neighbours.append((index, value))
        return neighbours
            
    def print_graph(self):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in self.matrix]))

