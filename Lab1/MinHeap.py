class minHeap:

    def __init__(self): 
        self.array = [] 
        self.size = 0
        self.pos = [] # Array for storing positions of vertices

    def add(self, vertex, weight): 
        newNode = [vertex, weight]
        self.array.append(newNode)
        self.pos.append(vertex)
        self.size += 1

    def isEmpty(self): 
        return self.size == 0

    def pop(self):
        if self.isEmpty() == True: 
            return
        # Store root and replace root with last node
        root = self.array[0]
        lastNode = self.array[self.size - 1] 
        self.array[0] = lastNode
        # Update position of last node 
        self.pos[lastNode[0]] = 0
        # Store position at pre-decremented heap size
        self.pos[root[0]] = self.size - 1
        # Reduce heap size and heapify root
        self.size -= 1
        self.heapify(0)
        return root

    # Utility function for swapping two nodes
    def swap(self, a, b): 
        t = self.array[a] 
        self.array[a] = self.array[b] 
        self.array[b] = t 

    # Nodes not in the heap will be indexed at larger values
    # than size the heapsize
    def inHeap(self, vertex): 
        if self.pos[vertex] < self.size: 
            return True
        return False

    # Edge weights are decreased when a lower edge weight for
    # a vertex in the heap has been found
    def decreaseWeight(self, vertex, weight):
        i = self.pos[vertex] 
        self.array[i][1] = weight
        # Heapify updated vertex upward
        while i > 0 and self.array[i][1] < self.array[int((i - 1) / 2)][1]: 
            # Swap this node with its parent 
            self.pos[ self.array[i][0] ] = int((i - 1) / 2)
            self.pos[ self.array[int((i - 1) / 2)][0] ] = i 
            self.swap(i, int((i - 1) / 2)) 
            # move to parent index 
            i = int((i - 1) / 2);


    def heapify(self, current):
        
        smallest = current 
        left = 2 * current + 1
        right = 2 * current + 2
        
        if left < self.size and self.array[left][1] < self.array[smallest][1]: 
            smallest = left
        if right < self.size and self.array[right][1] < self.array[smallest][1]: 
            smallest = right
            
        if smallest != current: 
            self.pos[ self.array[smallest][0] ] = current 
            self.pos[ self.array[current][0] ] = smallest 
            self.swap(smallest, current) 
            self.heapify(smallest)
