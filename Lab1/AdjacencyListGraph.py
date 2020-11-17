import collections
import sys
from MinHeap import*

class Node:
    
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.next = None


class Graph:
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [None] * self.vertices

    # Method for adding an undirected edge between two nodes 
    def add_edge(self, source, destination, weight):
        if weight < 1:
            return
        
        # Create first node and link it to the source index
        node = Node(destination, weight)
        node.next = self.adj_list[source]
        self.adj_list[source] = node
        
        # Create second node and link it to the destination index
        node = Node(source, weight)
        node.next = self.adj_list[destination]
        self.adj_list[destination] = node

    # Traverses the graph and checks if it is connected
    def is_connected(self):
        fifo = collections.deque()
        visited = [False] * self.vertices

        fifo.append(0)
        count = 0
        while len(fifo) > 0:
            vertex = fifo.popleft()
            node = self.adj_list[vertex]
            if not visited[vertex]:
                visited[vertex] = True
                count += 1
                print("Visiting vertex: ", vertex)
                while node!=None:
                    fifo.append(node.value)
                    node = node.next
        return count == self.vertices

    # Prints the graph
    def print_graph(self):
        for i in range(self.vertices):
            print("Vertex " + str(i) + ":", end="")
            temp = self.adj_list[i]
            while temp:
                print(" -> {}".format(temp.value),
                      "( weight: {}".format(temp.weight),
                      ")", end="")
                temp = temp.next
            print(" \n")


    # Prints a minimum spanning tree
    def printMST(self, tree, edge_weights): 
        print ("Edge \tWeight")
        for i in range(1, self.vertices): 
            print (tree[i], "-", i, "\t", edge_weights[i])

    
    # Returns index of the vertex with lowest edge weight from
    # unpicked vertices in MST
    def minWeight(self, edge_weights, mstSet):
        min = sys.maxsize

        for vertex in range(self.vertices):
            # If the edge_weight is the lowest one, and the vertex
            # has not been picked
            if edge_weights[vertex] < min and not mstSet[vertex]:
                min = edge_weights[vertex]
                min_index = vertex
        return min_index

    
    def prim(self):
 
        edge_weights = [sys.maxsize] * self.vertices
        edge_weights[0] = 0
        mstSet = [False] * self.vertices # Picked vertices in the graph
        tree = [None] * self.vertices # Element is v1, index is connected v2

        for iteration in range(self.vertices):
            # Get vertex with lowest edge weight
            next_v = self.minWeight(edge_weights, mstSet)
            # Put vertex with lowest edge weight in mstSet
            mstSet[next_v] = True
            
            temp = self.adj_list[next_v]
            while temp:
                if not mstSet[temp.value] and edge_weights[temp.value] > temp.weight:
                    edge_weights[temp.value] = temp.weight
                    tree[temp.value] = next_v
                temp = temp.next
        self.printMST(tree, edge_weights)


    def prim_heap(self):

        edge_weights = [sys.maxsize] * self.vertices
        tree = [None] * self.vertices
        # Load all nodes to the heap
        heap = minHeap()
        for vertex in range(self.vertices):
            heap.add(vertex, sys.maxsize)

        heap.pos[0] = 0
        edge_weights[0] = 0
        heap.decreaseWeight(0, 0) 

        while heap.isEmpty() == False:
            
            current = heap.pop()
            temp = self.adj_list[current[0]]

            while temp:
                if heap.inHeap(temp.value) and edge_weights[temp.value] > temp.weight:
                    edge_weights[temp.value] = temp.weight
                    tree[temp.value] = current[0]
                    heap.decreaseWeight(temp.value, edge_weights[temp.value])
                temp = temp.next
        self.printMST(tree, edge_weights)




