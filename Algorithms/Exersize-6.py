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
5.

"""
"""
6. Use the Print Shortest Path algorithm (Algorithm 3.5) to find the shortest path from vertex v7 to vertex v3, in the graph of Exercise 5, using the matrix
P found in that exercise. Show the actions step by step.

Solution:

"""
"""
7. Analyze the Print Shortest Path algorithm (Algorithm 3.5) and show that it has a linear-time complexity.

Solution: the print shortest path algorithm has a linear time complexity because it only iterates through the P matrix once.


"""
"""
12. List all of the different orders in which we can multiply five matrices A, B, C, D, and E.


"""

"""
13. 
"""

