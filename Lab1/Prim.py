#from AdjacencyListGraph import*
from AdjacencyMatrixGraph import*
from GraphGenerator import*

# Finds a minimal spanning tree with prims algorithm, returns the
# tree as a graph
def prim_matrix(graph):
    MST = Graph(graph.size)
    no_edges = 0 # Number of edges
    selected = [False] * graph.size
    selected[0] = True # Start at vertex 0
    while (no_edges < graph.size - 1): # While E < V - 1
        minimum = sys.maxsize
        x = 0
        y = 0
        for i in range(graph.size):
            if selected[i]:
                for j in range(graph.size):
                    edge = graph.matrix[i][j]
                    if not selected[j] and edge > 0:
                        if minimum > edge:
                            minimum = edge
                            x = i
                            y = j
        MST.add_edge(x, y, minimum)
        selected[y] = True
        no_edges += 1
    return MST


def main():
    g = GraphGenerator()
    graphs = g.get_graphs(1, 7, 3)
    for graph in graphs:
        graph.print_graph()
        print('\n')
        MST = prim_matrix(graph)
        MST.print_graph()

if __name__ == "__main__":
    main()
