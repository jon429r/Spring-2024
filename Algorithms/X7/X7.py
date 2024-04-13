"""
4. Draw a graph that has more than one minimum spanning tree.a

For solution see Question_4.jpg for solution

"""
"""
5. Implement Prim’s algorithm (Algorithm 4.1) on your system, and study its performance using 
different graphs.
"""


def Prim(n, W):
    """
    Determines a minimum spanning tree.

    args:
    n -- integer: n >= 2
    W[i][j] -- 2D array: A connected, weighted, undirected graph containing n vertices, 
    represented by W.
    W[i][j] is the weight on the edge from the ith vertex to the jth vertex.

    returns: list of tuples: The minimum spanning tree represented as a set of edges.
    """
 
    #Starts with empty set of edges
    mst = []
    mst_edges = []

    # Start at v0
    mst.append(0)
    
    #Iterate while all vertices are not in mst
    while len(mst) < n:
        # Initialize values
        minimum_weight = float('inf')
        minimum_edge = None
        
        # Loop through mst check the values in the mst to see if there are 
        # lesser values in the graph
        for i in mst:
            for j in range(n):
                if j not in mst and W[i][j] < minimum_weight:
                    minimum_weight = W[i][j]
                    minimum_edge = (i, j)

        i, j = minimum_edge
        mst.append(j)
        mst_edges.append((i, j, minimum_weight))

    return mst_edges

W = [
    [0, 1, 3, float('inf'), float('inf')],
    [1, 0, 3, 6, float('inf')],
    [3, 3, 0, 4, 2],
    [float('inf'), 6, 84, 0, 5],
    [float('inf'), float('inf'), 2, 5, 0]
]

############################### output using Figure 4.3(a) #########################################
# Minimum Spanning Tree Edges:
# Starting vertex, Ending vertex, Weight
# (0, 1, 1)
# (0, 2, 3)
# (2, 4, 2)
# (2, 3, 4)
####################################################################################################

n = len(W)
minimum_spanning_tree = Prim(n, W)
print("Minimum Spanning Tree Edges (Prim's algo): \nStarting vertex, Ending vertex, Weight")
for edge in minimum_spanning_tree:
    print(edge)


"""
7. Use Kruskal’s algorithm (Algorithm 4.2) to find a minimum spanning tree for the graph in Exercise 2. Show the actions step by step.

Empty set of weights sorted
(4, 8, 3)
(8, 9, 4)
(7, 3, 5)
(6, 10, 6)
(4, 5, 10)
(9, 10, 12)
(1, 4, 17)
(3, 4, 18)
(5, 9, 25)
(5, 6, 28)
(1, 2, 32)
(5, 2, 45)
(7, 8, 59)

Add (4,8,3)
Add (8,9,4)
Add (7,3,5)
Add (6,10,6)
Add (4,5,10)
Add (9,10,12)
Add (1,4,17)
Add (3,4,18)
Add (5,9,25) Would create a cycle, Remove
Add (5,6,28) Would create a cycle, Remove
Add (1,2,32)
Add (5,2,45) Would create a cycle, Remove
Add (7,8,59) Would create a cycle, Remove

The process is completed. The resulting minimum spanning tree consists of the following edges:

(4,8,3)
(8,9,4)
(7,3,5)
(6,10,6)
(4,5,10)
(9,10,12)
(1,4,17)
(3,4,18)
(1,2,32)

"""


"""
8. Implement Kruskal’s algorithm (Algorithm 4.2) on your system, and study its performance 
using different graphs.
"""

def Kruskal(W, n):
    """
    Determines the minimum spanning tree

    Args:
    W -- 2D array: A connected, weighted graph containing n vertices,
         where W[i][j] is the weight on the edge from the ith vertex to the jth vertex.
    n -- integer: Number of vertices (n >= 2)

    Output:
    A list of edges in a minimum spanning tree
    """
    mst_edges = []
    edges = []

    # Get all edges from the graph represented by W
    for i in range(n):
        for j in range(i+1, n):
            if W[i][j] != float('inf'):
                edges.append((i, j, W[i][j]))

    # Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[2])

    # Initialize a list to keep track of vertices included in MST
    used_vert = [False] * n

    # Iterate through sorted edges
    for edge in sorted_edges:
        u, v, weight = edge
        # if vertex has not been used
        if not used_vert[u] or not used_vert[v]:
            mst_edges.append(edge)
            used_vert[u] = True
            used_vert[v] = True
        # If both vertices are already included and adding this edge creates a cycle, skip it
        elif used_vert[u] and used_vert[v]:
            continue

    return mst_edges



W = [
    [0, 1, 3, float('inf'), float('inf')],
    [1, 0, 3, 6, float('inf')],
    [3, 3, 0, 4, 2],
    [float('inf'), 6, 84, 0, 5],
    [float('inf'), float('inf'), 2, 5, 0]
]

n = len(W)
minimum_spanning_tree = Kruskal(W,n)
print("Minimum Spanning Tree Edges (Kruskal's algo): \nStarting vertex, Ending vertex, Weight")
for edge in minimum_spanning_tree:
    print(edge)

"""
14. Implement Dijkstra’s algorithm (Algorithm 4.3) on your system, and study its performance using different graphs.
"""

def Dijkstra(W, n):
    """
    Determines the shortest paths from v1 to all other vertices in a weighted,
    directed graph.

    Args:
    n -- integer: n >= 2
    W -- 2D array: A connected, weighted, directed graph containing n vertices,
         where W[i][j] is the weight on the edge from the ith vertex to the jth vertex.

    Returns:
    A list of edges containing the shortest path
    """
    # Initialize a list to keep track of the shortest distances from v1 to all other vertices
    distances = [float('inf')] * n
    distances[0] = 0  # Distance from v1 to itself is 0

    # Initialize a list to keep track of the predecessor vertex for each vertex
    predecessors = [None] * n

    # Initialize a list to keep track of visited vertices
    visited = [False] * n

    # Main loop
    for _ in range(n):
        # Find the vertex with the minimum distance among unvisited vertices
        min_distance = float('inf')
        u = -1
        for i in range(n):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                u = i

        # Mark the vertex as visited
        visited[u] = True

        # Update the distances and predecessors of neighboring vertices
        for v in range(n):
            if not visited[v] and W[u][v] != float('inf'):
                if distances[u] + W[u][v] < distances[v]:
                    distances[v] = distances[u] + W[u][v]
                    predecessors[v] = u

    # Construct the shortest path as a list of edges
    mst_edges = []
    for v in range(1, n):  # Skip v1
        if predecessors[v] is not None:
            edge = (predecessors[v], v, W[predecessors[v]][v])
            mst_edges.append(edge)

    return mst_edges


W = [
    [0, 1, 3, float('inf'), float('inf')],
    [1, 0, 3, 6, float('inf')],
    [3, 3, 0, 4, 2],
    [float('inf'), 6, 84, 0, 5],
    [float('inf'), float('inf'), 2, 5, 0]
]

n = len(W)
minimum_spanning_tree = Dijkstra(W,n)
print("Minimum Spanning Tree Edges (Dijkstra's algo): \nStarting vertex, Ending vertex, Weight")
for edge in minimum_spanning_tree:
    print(edge)

"""
28. Decode each bit string using the binary code in Exercise 24. 
(a) 01100010101010 -> (1*2^12)+(1*2^11)+(1*2^7)+(1*2^5)+(1*2^3)+(1*2^1) -> 4096 + 2048 + 128 + 32 + 8 + 2 = 6,314
(b) 1000100001010  -> (1*2^12) + (1*2^8) + (1*2^3) + (1*2^1) = 4096 + 256 + 8 + 2 -> 4,362
(c) 11100100111101 -> (1*2^13)+(1*2^12)+(1*2^11)+(1*2^8)+(1*2^5)+(1*2^4)+(1*2^3)+(1*2^2)+(1*2^0) -> 8192 + 4096 + 2048 + 256 + 32 + 16 + 8 + 4 + 1 = 14,653
(d) 1000010011100  -> 1*2^12 + 1*2^7 + 1*2^4 + 1*2^3 + 1*2^2 -> 4096 + 128 + 16 + 8 + 4 -> 4252
"""
