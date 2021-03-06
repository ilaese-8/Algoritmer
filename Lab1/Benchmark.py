from GraphGenerator import*
import time


class Benchmark:


    def unsortedPrim(self, graphs, amount, graphSize):
        before = time.perf_counter()
        for graph in graphs:
            graph.prim()
        after = time.perf_counter() - before
        
        print("Time to perform prims algorithm on ", amount,
              " graphs, of ", graphSize,
              " vertices: using unsorted lists: ",
              after, " seconds")
              
        print("Average time per algorithm: ", after/amount,
              " seconds")
        

    def heapPrim(self, graphs, amount, graphSize):
        before = time.perf_counter()
        for graph in graphs:
            graph.prim_heap()
        after = time.perf_counter() - before
        
        print("Time to perform prims algorithm on ", amount,
              " graphs, of ", graphSize,
              " vertices using binary heap: ",
              after, " seconds")
              
        print("Average time per algorithm: ", after/amount,
              " seconds")

        
def main():
    
    g = GraphGenerator()
    b = Benchmark()

    amount = 10
    vertices = 3000
    connection_density = 3
    
    graphs = g.get_graphs(amount, vertices, connection_density)
    
    b.unsortedPrim(graphs, amount, vertices)
    b.heapPrim(graphs, amount, vertices)

if __name__ == "__main__":
    main()
