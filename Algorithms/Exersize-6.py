"""
1. Establish Equality 3.1 given in this section.

original equation: (n k) = n! / (k! * (n-k)!) for 0 <= k <= n

Equality 3.1: (n k) = (n-1 k-1) + (n-1 k) for 0 < k < n, k = 0 or k = n

Solution: 
Proof by induction:
Base case: k = 0, n = 0

The binomial coefficient of 0 and 0 is 1

using the original equation:
(0 0) = 0! / (0! * (0-0)!) = 1

using the equality 3.1:
(0 0) = (0-1 0-1) + (0-1 0) = (0 0) = 1

Inductive step:
Assume the equality holds for n and k

(n+1 k) = (n k-1) + (n k)

expand:

(n+1 k) + (n k) = [(n-1 k-1)-1 + (n-1 k-1)] + [(n-1 k-1) + (n-1 k)]

simpify:

= (n-1 k-1) + (n-1 k) + (n-1 k-1) + (n-1 k)

combine like terms:

= (n-1 k) + (n-1 k-1) + (n-1 k) + (n-1 k-1) + (n-1 k) + (n-1 k)

= 2(n k)

= (n+1 k)


"""
"""
3. Implement both algorithms for the Binomial Coefficient problem (Algorithms 3.1 and 3.2) on your system and study their performances using different problem instances.
"""

def bin_coeffienct_divacon(n , k) -> int:
    """
    calculate binomial coeffienct using divide and concur

    args: n
    args: k
    """
    if(k in (0, n)):
        return 1
    else:
        return bin_coeffienct_divacon(n-1, k-1) + bin_coeffienct_divacon(n-1, k)

print(f'binomial coeffienct of 5 and 2 is {bin_coeffienct_divacon(5, 2)}')
print(f'binomial coeffienct of 10 and 4 is {bin_coeffienct_divacon(10, 4)}')

def bin_coeffienct_dp(n, k) -> int:
    """
    calculate binomial coeffienct using dynamic programming

    args: n
    args: k
    """
    B = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k)+1):
            if(j in (0, i)):
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]
    return B[n][k]

print(f'binomial coeffienct of 5 and 2 is {bin_coeffienct_dp(5, 2)}')
print(f'binomial coeffienct of 10 and 4 is {bin_coeffienct_dp(10, 4)}')


"""
4. Modify Algorithm 3.2 (Binomial Coefficient Using Dynamic Programming) so that it uses only a one-dimensional array indexed from 0 to k.
"""

def mod_bin_coeffienct_dp(n, k) -> int:
    """
        Modified Algo 3.2 so that it uses only a demensional array indexed from 0 to k.

        args: n
        args: k
    """
    B = [0 for _ in range(k+1)]
    B[0] = 1

    for i in range(1, n+1):
        for j in range(min(i, k), 0, -1):
            B[j] = B[j] + B[j-1]
    return B[k]


"""
5. Use Floyd's algorithm for the shortest paths problem 2 (algorithm 3.4) to construct the matrix D,
which contains the lengths of the shortest paths, and the matrix P, which contains the highest indices of the intermediate vertices
on the shortest paths, for the following graph show the actions step by step

Solution: 

P = 

0|1 |2 |3 |4 |5 |6 |7
1|0 |4 |9 |8 |9 |26|16|
2|3 |0 |6 |5 |6 |23|13|
3|9 |32|0 |14|12|32|22|
4|8 |18|24|0 |1 |18|8 |
5|9 |20|26|1 |0 |19|10|
6|26|23|33|18|19|0 |26|
7|15|13|22|8 |6 |10|0 |

P = [[0,4,9,8,9,26,16],[3,0,6,5,6,23,13],[9,32,0,14,12,32,22],[8,18,24,0,1,18,8],[9,20,26,1,0,19,10],[26,23,33,18,19,0,26],[15,13,22,8,6,10,0]]

"""
"""
6. Use the Print Shortest Path algorithm (Algorithm 3.5) to find the shortest path from vertex v7 to vertex v3, in the graph of Exercise 5, using the matrix
P found in that exercise. Show the actions step by step.

Solution:

P = [[0,4,9,8,9,26,16],[3,0,6,5,6,23,13],[9,32,0,14,12,32,22],[8,18,24,0,1,18,8],[9,20,26,1,0,19,10],[26,23,33,18,19,0,26],[15,13,22,8,6,10,0]]

The shortest path from v7 to v3 is v7 -> v4 -> v5 -> v3
"""

"""
7. Analyze the Print Shortest Path algorithm (Algorithm 3.5) and show that it has a linear-time complexity.

Solution: the print shortest path algorithm has a linear time complexity because it only iterates through the P matrix once.
"""

"""
12. List all of the different orders in which we can multiply five matrices A, B, C, D, and E.

Catalan number: 
n = m-1, Cn = (2n)! / (n+1)!n!
C(4) = 2(4)! / (4+1)! * 4!
C(4) = 8! / 5! * 4!
C(4) = 40320 / 120 * 24
C(4) = 40320 / 2880
C(4) = 14

There are 14 different ways to multiply 5 matrices

The 14 combinations are:
1. (A*B*C*D*E)
2. ((A*B)*(C*D*E))
3. ((A*B*C)*(D*E))
4. (A*B)*(C*D)*(E)
5. (A*(B*C))*(D*E)
6. (A*(B*C*D))*E
7. ((A*B)*(C*D))*E
8. (A*((B*C)*D))*E
9. (A*(B*(C*D)))*E
10. (A*((B*C)*D*E))
11. ((A*B)*(C*D))*E
12. (A*((B*C)*D))*E
13. (A*(B*(C*D)))*E
14. (A*(B*C))*(D*E)


"""

"""
13. Find the optimal order and its cost for evaluating the product A1 * A2 * A3 * A4 * A5
where
A1 = 10x4
A2 = 4x5
A3 = 5x20
A4 = 20x2
A5 = 2x50

Show the final matrices M and P produced by algorithm 3.6

Solution:

"""

def minmult(n, d, P):
    """
    Docstring
    """
    M = [[0] * n for _ in range(n)]
    for i in range(1, n):
        M[i][i] = 0
    
    for diagonal in range(1, n - 1):
        for i in range(1, n - diagonal):
            j = i + diagonal
            M[i][j] = float('inf')
            for k in range(i, j):
                cost = M[i][k] + M[k+1][j] + d[i-1] * d[k] * d[j]
                if cost < M[i][j]:
                    M[i][j] = cost
                    P[i][j] = k


    # print Final matrix M, Final matrix P, optimal_cost, optimal_order
    print(f'Final matrix M: \n{M}')
    print(f'Final matrix P: \n{P}')
    print(f'Optimal cost: \n{M[1][n-1]}')
    print(f'Optimal order: \n{P}')
    return M[1][n-1]


# Matrix dimensions
d = [10, 4, 5, 20, 2, 50]
n = len(d) - 1
P = [[0] * n for _ in range(n)]  

minmult(n, d, P)

########################## Output ##########################################
#Final matrix M: [[0, 0, 0, 0, 0], [0, 0, 200, 1200, 320], [0, 0, 0, 400, 240], [0, 0, 0, 0, 200], [0, 0, 0, 0, 0]]
#Final matrix P: [[0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 0, 0, 2, 2], [0, 0, 0, 0, 3], [0, 0, 0, 0, 0]]
#Optimal cost: 320
# Optimal order:[[0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 0, 0, 2, 2], [0, 0, 0, 0, 3], [0, 0, 0, 0, 0]]
