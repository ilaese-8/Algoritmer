import collections
import sys

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

    # Traverses the graph and checks if it is connected
    def is_connected(self):
        fifo = collections.deque()
        visited = [False] * self.size

        fifo.append(0)
        count = 0
        while len(fifo) > 0:
            vertex = fifo.popleft()
            if not visited[vertex]:
                visited[vertex] = True
                count += 1
                print("Visiting vertex: ", vertex)
                for i in range(self.size):
                    if self.matrix[vertex][i] > 0:
                        fifo.append(i)
        return count == self.size

    # Prints the graph
    def print_graph(self):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in self.matrix]))

    # Find a minimal spanning tree with prims algorithm, returns the
    # tree as a graph
    def prim(self):
        no_edges = 0 # Number of edges
        selected = [False] * self.size
        selected[0] = True
        while (no_edges < self.size - 1): # While E < V - 1
            minimum = sys.maxsize
            x = 0
            y = 0
            for i in range(self.size):
                if selected[i]:
                    for j in range(self.size):
                        if not selected[j] and self.matrix[i][j] > 0:
                            if minimum > self.matrix[i][j]:
                                minimum = self.matrix[i][j]
                                x = i
                                y = j
            print(str(x) + "-" + str(y) + ":" + str(self.matrix[x][y]))
            selected[y] = True
            no_edges += 1
                        
        
        
        








    
