import collections

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

