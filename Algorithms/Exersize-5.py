"""# 18, 19, 21, 22, 25, 26, 27, 28, 32, 34, 35"""
# Best 8 out of 11
# Completion status: 8/11

# 18

# 19: complete

"""
Use Quicksort (Algorithm 2.6) to sort the following list. Show the actions step by step.
[123, 24, 189, 56, 150, 12, 9, 240]
pivot = 123
[24, 56, 12, 9, 123, 189, 150, 240]
123 is in the correct position
partition 1: [24, 56, 12, 9] partition 2: [189, 150, 240]
pivot1 = 24 pivot2 = 189
partition1: [12, 56, 24, 9] partition2: [150, 189, 240]
pivot1 = 12, pivot2 = 24
partition1: [12, 56] partition2: [9, 24]

final sorted list: [9, 12, 24, 56, 123, 150, 189, 240]
"""

# 21

# 22

# 25: complete

"""
The number of additions performed by algorithm 1.4 can be 
reduced by modifying the algorithm to not add the elements
of the matrix that are multiplied by 0. The number of additions can be
reduced by n^2 - n, where n is the number of elements in the
matrix.
"""

# 26: Complete

"""
In Example 2.4, we gave Strassen’s product of two 2 × 2 
matrices. Verify the correctness of this product.
"""

"""
m1 = (A[0][0] + A[1][1]) * (B[0][0] + B[1][1])
m2 = (A[1][0] + A[1][1]) * B[0][0]
m3 = A[0][0] * (B[0][1] - B[1][1])
m4 = A[1][1] * (B[1][0] - B[0][0])
m5 = (A[0][0] + A[0][1]) * B[1][1]
m6 = (A[1][0] - A[0][0]) * (B[0][0] + B[0][1])
m7 = (A[0][1] - A[1][1]) * (B[1][0] + B[1][1])


If A = [2 4; 1 3] and B = [5 7; 6 8]

m1 = (2 + 3) * (5 + 8) = 5 * 13 = 65
m2 = (1 + 3) * 5 = 4 * 5 = 20
m3 = 2 * (7 - 8) = 2 * -1 = -2
m4 = 3 * (8 - 5) = 3 * 3 = 9
m5 = (2 + 4) * 8 = 6 * 8 = 48
m6 = (1 - 2) * (5 + 7) = -1 * 12 = -12
m7 = (4 - 3) * (6 + 8) = 1 * 14 = 14

C[0][0] = 65 + 9 - 48 + 14 = 40
C[0][1] = -2 + 48 = 46
C[1][0] = 20 + 9 = 29
C[1][1] = 65 - 20 - 2 - 12 = 31

C = [40 46; 29 31]

"""

# 27: Complete

"""
If its a 64 * 64 matrix, and the standard algorithm is N^3, the total number of multiplications are
64^3 = 262,144
"""

# 28: Complete

"""
The time complexity of Strassen's algorithm is N^log7, the total number of multiplications are
64^log7 = 117,649
"""
# 32: Complete

def divide(u, m):
    quotient = 0
    while u >= m:
        u -= m
        quotient += 1
    return quotient, u

print(divide(10, 3))
print(divide(10, 5))

""" This is a linear time complexity algorithm because the while loop runs until u is less than m.
The time complexity is O(u/m) while is linear. """

# 34: Complete
"""
Implement both Exchange Sort and Quicksort algorithms on your computer to sort a list of n elements. 
Find the lower bound for n that justifies application of the Quicksort algorithm with its overhead.
"""

def Quicksort(X):
    if len(X) <= 1: # base case
        return X
    pivot = X[0] # pivot element is the first element
    less = [x for x in X if x < pivot] # for elements less than pivot
    greater = [x for x in X if x > pivot] # for elements greater than pivot
    return Quicksort(less) + [pivot] + Quicksort(greater) # recursive call

print(Quicksort([3,1,2]))
print(Quicksort([4,10,3,5,1,2,6,9,2,9]))
print(Quicksort([100, 34,23,30,76, 11,35,56]))

def ExchangeSort(X):
    for i in range(len(X)): # for each element in the list
        for j in range(i+1, len(X)): # for each element after the current element
            if X[i] > X[j]: # if the current element is greater than the next element
                X[i], X[j] = X[j], X[i] # swap the elements
    return X

print(ExchangeSort([3,1,2]))
print(ExchangeSort([4,10,3,5,1,2,6,9,2,9]))
print(ExchangeSort([100, 34,23,30,76, 11,35,56]))


# 35: Complete
"""
Implement both the standard algorithm and Strassen’s algorithm on your computer to 
multiply two n × n matrices (n = 2k). Find the lower bound for n that justifies 
application of Strassen’s algorithm with its overhead.
"""

def standard_algo(A, B):
    C = [[0 for i in range(len(A))] for j in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

def Strassens_algo(A, B):
    C = [[0 for i in range(len(A))] for j in range(len(B[0]))]
    m1 = (A[0][0] + A[1][1]) * (B[0][0] + B[1][1])
    m2 = (A[1][0] + A[1][1]) * B[0][0]
    m3 = A[0][0] * (B[0][1] - B[1][1])
    m4 = A[1][1] * (B[1][0] - B[0][0])
    m5 = (A[0][0] + A[0][1]) * B[1][1]
    m6 = (A[1][0] - A[0][0]) * (B[0][0] + B[0][1])
    m7 = (A[0][1] - A[1][1]) * (B[1][0] + B[1][1])
    C[0][0] = m1 + m4 - m5 + m7
    C[0][1] = m3 + m5
    C[1][0] = m2 + m4
    C[1][1] = m1 - m2 + m3 + m6
    return C


A = [[2, 4], [1, 3]]
B = [[5, 7], [6, 8]]
C = [[0, 0], [0, 0]]

print(f' C: {standard_algo(A, B)}')
print(f' C: {Strassens_algo(A, B)}')

"""
The lower bound for n that justifies the application of 
Strassen's algorithm is 64. In practice Strassen's algorithm
tends to outperform the standard algorithm when the size
of the matrix is 64 or greater.
"""
