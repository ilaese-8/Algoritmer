class Graph:

    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for i in range(size)] for j in range(size)] 

    # Method for adding an undirected edge between two nodes 
    def add_edge(self, vertex_one, vertex_two, weight):
        if weight < 1:
            return
        self.matrix[vertex_one][vertex_two] = weight
        self.matrix[vertex_two][vertex_one] = weight

    # Graph traversal method, prints traversed path and amount of nodes visited
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

