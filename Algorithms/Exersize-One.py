import random
import math

def smallestNum(arr):
    """ 1. Write an algo that finds the m smallest numbers in a list"""
    
    smallest = arr[0]
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

def subsetOf(arr):
    """Prints out all the subsets of three elements of a set of n elements"""
    n = len(arr)

    if n < 3:
        print("The array must contain 3 or more elements")
        return
    elif n == 3:
        print(arr)
        return
    
    combinations = []

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                subset = [arr[i], arr[j], arr[k]]
                combinations.append(subset)
                print(subset)
    
    return combinations


    
def insertionSort(arr):
    """Discuss and write the insertions sort algorithm
    
    Discussion: The insertion sort algorithm starts at the first element
    in an array. It uses 2 pointers on of which follows keeps track of the
    first element, the next pointer iterates through the array looking for
    elements smaller than the first. If it finds a smaller value it swaps the
    positions else it moves forward. Once all elements are iterated through
    and the smallest element is found the first pointer moves foward and the
    process is repeated to find the next smallest element.
    """
    for i in range(len(arr)):
        j = i
        temp = arr[j]
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = temp
    return arr

def GCD(n1, n2):
    """Write an algorithm to find the greatest common divisor of two integers"""
    n1Divisors = []
    n2Divisors = []
    for i in range(2, math.floor(n1/2)):
        temp = i
        if n1 % temp == 0:
            n1Divisors.append(temp)
    for i in range(2, math.floor(n2/2)):
        temp = i
        if n2 % temp == 0:
            n2Divisors.append(temp)
    print(n1Divisors, n2Divisors)

    commonDivisors = []
    for d in n1Divisors:
        if d in n2Divisors:
            commonDivisors.append(d)
    if(len(commonDivisors) != 0):
        GCD = commonDivisors[0]
    else:
        return 1

    for divisor in commonDivisors:
        if divisor > GCD:
            GCD = divisor
    return GCD
    

def main():
    testArray = [5, 3, 1, 2, 4]
    intArray = [random.randint(1, 1000) for i in range(100)]

    #smallest = smallestNum(intArray)
    #print(f'Smallest in array: {smallest}')

    #sortedArr = insertionSort(intArray)
    #print(sortedArr)

    #print(GCD(24, 18))

    subsetOf([1,2,3,4,5])

if __name__ == "__main__":
    main()