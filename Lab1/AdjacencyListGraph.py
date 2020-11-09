class Node:
    
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.next = None


class Graph:
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices

    # Method for adding an undirected edge between two nodes 
    def add_edge(self, source, destination, weight):
        if weight < 1:
            return
        
        # Create first node and link it to the source index
        node = Node(destination, weight)
        node.next = self.graph[source]
        self.graph[source] = node
        
        # Create second node and link it to the destination index
        node = Node(source, weight)
        node.next = self.graph[destination]
        self.graph[destination] = node

    # Graph traversal method, prints traversed path and amount of nodes visited
    def traverse(self):
        visited = [False] * self.vertices
        counter = 0

        # Iterate through all nodes
        for i in range(self.vertices):
            vertice = self.graph[i]

            # Go through all connected edges
            while vertice != None:
                val = vertice.value
                if not visited[val]:
                    print("Traversing through: ", val)
                    visited[val] = True
                    counter += 1
                vertice = vertice.next
                
        print(" \nNodes visited: ", counter)

