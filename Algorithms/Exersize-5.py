"""# 18, 19, 21, 22, 25, 26, 27, 28, 32, 34, 35"""

# 18

# 19

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

# 25

# 26

# 27

"""
If its a 64 * 64 matrix, and the standard algorithm is N^3, the total number of multiplications are
64^3 = 262,144
"""

# 28

"""
The time complexity of Strassen's algorithm is N^log7, the total number of multiplications are
64^log7 = 117,649
"""
# 32

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

# 34
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


# 35
"""
Implement both the standard algorithm and Strassen’s algorithm on your computer to 
multiply two n × n matrices (n = 2k). Find the lower bound for n that justifies 
application of Strassen’s algorithm with its overhead.
"""
