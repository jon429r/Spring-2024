
def Gaussian_elim(A, b):
    """
    Gaussian elimination with partial pivoting
    
    Solves a system of linear equations Ax = b using Gaussian elimination with partial pivoting.

    @arg: A--Matrix representing the coefficients of the linear equations
    @arg: b--Vector representing the constants on the right-hand side of the equations
    """
    print(f'Input Matrix: {A} \nInput Vector: {b}')
    # Get the size of the matrix
    n = len(A)

    # Initialize a modified matrix M to hold augmented matrix [A | b]
    M = A

    # Append the elements of b to the corresponding rows of M to form the augmented matrix
    i = 0
    for x in M:
        x.append(b[i])
        i += 1

    for k in range(n): # start in left column move to right
        for i in range(k, n): # loop though elements in column checking for larger elements that the pivot
            if abs(M[i][k]) > abs(M[k][k]):
                M[k], M[i] = M[i], M[k]

        
        for j in range(k + 1, n): # Eliminate the lesser elements than the pivot
            q = float(M[j][k]) / M[k][k]
            for m in range(k, n + 1):
                M[j][m] -= q * M[k][m]

    # Back substitution
    x = [0 for i in range(n)] # This will be the solution

    x[n - 1] = float(M[n - 1][n]) / M[n - 1][n - 1] # solve for last unknown

    for i in range(n - 2, -1, -1): # solve for remaining unknowns
        z = 0
        for j in range(i + 1, n):
            z += float(M[i][j]) * x[j]
        x[i] = float(M[i][n] - z) / M[i][i]
    
    # Print the solution vector
    print(f'Solution: {x}')

# Book Example 3.1.4: Book solution: 1/9, 5/9, 0, 1/3
# Code solution [0.11111111111111108, 0.5555555555555556, -8.034508730839949e-17, 0.33333333333333337]
A = [[2, 5, 5, 3],[3, 3, 1, 3], [1, 4, 1, 2],[5,5,1,2]]
b = [4,3,3,4]

Gaussian_elim(A, b)
