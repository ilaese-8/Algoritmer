import collections

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
    


