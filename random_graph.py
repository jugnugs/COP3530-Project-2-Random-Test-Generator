from sys import argv

from igraph import Graph
import exrex

if __name__ == "__main__":
    numVertices = int(argv[1])
    numEdges = int(argv[2])
    powerIterations = int(argv[3])
    g = Graph.Erdos_Renyi(numVertices, m=numEdges, directed=True)
    edges = g.get_edgelist()

    nodeNames = {}

    vert = g.vs
    for vertex in vert:
        name = exrex.getone("[a-z0-9]{3,10}\.[a-z]{3}")
        nodeNames[vertex.index] = name

    file = open("results.txt", "w")
    file.write("{} {}\n".format(numEdges, powerIterations))
    for edge in edges:
        v1 = nodeNames[edge[0]]
        v2 = nodeNames[edge[1]]
        file.write("{v1} {v2}\n".format(v1=v1, v2=v2))
    file.close()