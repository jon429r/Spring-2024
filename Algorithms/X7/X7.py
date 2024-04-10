"""
4. Draw a graph that has more than one minimum spanning tree.
"""
"""
5. Implement Prim’s algorithm (Algorithm 4.1) on your system, and study its performance using different graphs.
"""

def Prim(n, W):
    """
    Determines a minimum spanning tree.

    args:
    n -- integer: n >= 2
    W[i][j] -- 2D array: A connected, weighted, directed graph containing n vertices, represented by W     ■ Line too long (102/100)
    W [i] [j] is the weight on the edge from the ith vertex to the jth vertex.

    returns: W -- The minimum spanning tree
   """
    pass

"""
7. Use Kruskal’s algorithm (Algorithm 4.2) to find a minimum spanning tree for the graph in Exercise 2. Show the actions step by step.
"""
"""
8. Implement Kruskal’s algorithm (Algorithm 4.2) on your system, and study its performance using different graphs.
"""

def Kruskal(n, m, E):
    """
    Determines the minimum spanning tree

    args:
    n -- integer >= 2
    m -- integer
    E -- The graph is represented by a set E that contains the edges in the graph along with their weights.

    output: A set of edges in a minimum spanning tree
    """
    pass

"""
14. Implement Dijkstra’s algorithm (Algorithm 4.3) on your system, and study its performance using different graphs.
"""

def Dijkstra(n, W):
    """
    Determines the shortest paths from v1 to all other vertices in a weighted,
    directed graph.

    args: 
    n -- integer: n >= 2
    W[i][j] -- 2D array: A connected, weighted, directed graph containing n vertices, represented by W
    W [i] [j] is the weight on the edge from the ith vertex to the jth vertex.

    returns: W -- A set of edges containing the shortest path
    """

    F = []

# graph representation
# 0 v1 v2 v3 v4 v5
# v1 0 7  4  6  1
# v2 N 0  N  N  N
# v3 N 2  0  5  N
# v4 N 3 N  0  N
# v5 N 4 N  1  0



"""
28. Decode each bit string using the binary code in Exercise 24. 
(a) 01100010101010 -> (1*2^12)+(1*2^11)+(1*2^7)+(1*2^5)+(1*2^3)+(1*2^1) -> 4096 + 2048 + 128 + 32 + 8 + 2 = 6,314
(b) 1000100001010  -> (1*2^12) + (1*2^8) + (1*2^3) + (1*2^1) = 4096 + 256 + 8 + 2 -> 4,362
(c) 11100100111101 -> (1*2^13)+(1*2^12)+(1*2^11)+(1*2^8)+(1*2^5)+(1*2^4)+(1*2^3)+(1*2^2)+(1*2^0) -> 8192 + 4096 + 2048 + 256 + 32 + 16 + 8 + 4 + 1 = 14,653
(d) 1000010011100  -> 1*2^12 + 1*2^7 + 1*2^4 + 1*2^3 + 1*2^2 -> 4096 + 128 + 16 + 8 + 4 -> 4252
"""
