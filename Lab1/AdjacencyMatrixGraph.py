class Graph:

    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for i in range(size)] for j in range(size)] 

    def add_edge(self, vertice_one, vertice_two, weight):
        if weight < 1:
            return
        self.matrix[vertice_one][vertice_two] = weight
        self.matrix[vertice_two][vertice_one] = weight

    def traverse(self):
        visited = [False] * self.size
        counter = 0
        for i in range(self.size):
            for j in range (self.size):
                if not visited[j] and self.matrix[i][j] > 0:
                    print("Traversing through: ", j)
                    visited[j] = True
                    counter += 1
        print("Nodes visited: ", counter)

    
