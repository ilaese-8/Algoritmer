import collections
import sys
from MinHeap import*

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

    # Prints a minimum spanning tree
    def printMST(self, tree): 
        print ("Edge \tWeight")
        for i in range(1, self.size): 
            print (tree[i], "-", i, "\t", self.matrix[i][ tree[i] ])


        # Returns index of the vertex with lowest edge weight from
        # unpicked vertices in MST
    def minWeight(self, edge_weights, mstSet):
        min = sys.maxsize
        for vertex in range(self.size):
            # If the edge_weight is the lowest one, and the vertex
            # has not been picked
            if edge_weights[vertex] < min and not mstSet[vertex]:
                min = edge_weights[vertex]
                min_index = vertex
        return min_index

    # Finds a minimum spanning tree with prims algorithm and prints it
    def prim(self):
        edge_weights = [sys.maxsize] * self.size
        edge_weights[0] = 0
        mstSet = [False] * self.size # Picked vertices in the graph
        tree = [None] * self.size # Element is v1, index is connected v2    
        for iteration in range(self.size):
            # Get vertex with lowest edge weight
            next_v = self.minWeight(edge_weights, mstSet)
            # Put vertex with lowest edge weight in mstSet
            mstSet[next_v] = True 
            for i in range(self.size):
                edge = self.matrix[next_v][i]
                if edge > 0 and not mstSet[i] and edge_weights[i] > edge:
                    edge_weights[i] = edge
                    tree[i] = next_v
        self.printMST(tree)


    def prim_heap(self):
        edge_weights = [sys.maxsize] * self.size
        tree = [None] * self.size
        
        # Load all vertices to the heap
        heap = minHeap()
        for vertex in range(self.size):
            heap.add(vertex, sys.maxsize)
            
        # Initialize starter vertex
        heap.pos[0] = 0
        edge_weights[0] = 0
        heap.decreaseWeight(0, 0)

        while heap.isEmpty() == False:
            current = heap.pop()
            for i in range(self.size):
                edge = self.matrix[current[0]][i]
                if edge > 0 and heap.inHeap(i) and edge_weights[i] > edge:
                    edge_weights[i] = edge
                    tree[i] = current[0]
                    heap.decreaseWeight(i, edge)
        self.printMST(tree)
