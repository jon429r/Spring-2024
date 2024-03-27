
function Gaussian_elim(A, b)
    """
    Gaussian elimination with partial pivoting

    Solves a system of linear equations Ax = b using Gaussian elimination with partial pivoting.

    Arguments:
    - A: Matrix representing the coefficients of the linear equations
    - b: Vector representing the constants on the right-hand side of the equations
    """
    println("Input Matrix A size: ", size(A), "\nInput Vector b size: ", size(b))
    # Get the size of the matrix
    n = size(A, 1)

    # Initialize a modified matrix M to hold augmented matrix [A | b]
    M = [A b]

    println("Augmented Matrix M size: ", size(M))

    for k in 1:n # start in left column move to right
        pivot = M[k, k]
        for i in k+1:n # loop through elements in column checking for larger elements that the pivot
            if abs(M[i, k]) > abs(pivot)
                pivot = M[i, k]
                M[k, :], M[i, :] = M[i, :], M[k, :]  # Swap rows
            end
        end

        for j in k + 1:n # Eliminate the lesser elements than the pivot
            q = M[j, k] / pivot
            M[j, k:end] .-= q * M[k, k:end]
        end
    end

    # Back substitution
    x = zeros(n) # This will be the solution
    x[n] = M[n, end] / M[n, n] # solve for last unknown

    println("Solution vector x size: ", size(x))

    for i in n - 1:-1:1 # solve for remaining unknowns
        z = 0
        for j in i+1:n
            z += M[i, j] * x[j]
        end
        x[i] = (M[i, end] - z) / M[i, i]  # Corrected index for last column of M
    end

    # Print the solution vector
    println("Solution: ", x)
end

# Example usage
A = [2.0 5.0 5.0 3.0; 3.0 3.0 1.0 3.0; 1.0 4.0 1.0 2.0; 5.0 5.0 1.0 2.0]
b = [4.0, 3.0, 3.0, 4.0]  # Float64 values

# Book Example 3.1.4: Book solution: 1/9, 5/9, 0, 1/3
# Code Solution: [0.11111111111111108, 0.5555555555555556,
# -8.034508730839949e-17, 0.33333333333333337]

Gaussian_elim(A, b)

