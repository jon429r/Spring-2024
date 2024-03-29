#
#3.2.1
#

A = [ 1 2 1 -1; 3 2 4 4; 4 4 3 4; 2 0 1 5]
U = [ 1 2 1 -1; 0 -4 1 7; 0 0 -2 1; 0 0 0 -1]

#a
# Define the elementary row matrices
M21 = [1 0 0 0; -3 1 0 0; 0 0 1 0; 0 0 0 1]
M31 = [1 0 0 0; 0 1 0 0; -4 0 1 0; 0 0 0 1]
M41 = [ 1 0 0 0; 0 1 0 0; 0 0 1 0; -2 0 0 1]

M32 = [1 0 0 0; 0 1 0 0; 0 -1 1 0; 0 0 0 1]
M42 = [1 0 0 0; 0 1 0 0; 0 0 1 0 ; 0 -1 0 1]

M43 = [1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 -1 1]


# Compute the matrix products
M1 = M41 * M31 * M21
M2 = M42 * M32 

# m1 = 1 0 0 0
#      -3 1 0 0
#      -4 0 1 0
#      -2 0 0 1
#
# m2 = 1 0 0 0
#      0 1 0 0
#      0 -1 0 1
#
# What patterns do you observe in these products?
# M1 is a unit lower triangular matrix
# M2 is a 4x3 matrix which is close to a unit lower triangular matrix

println("Matrix M(1):")
println(M1)
println("Matrix M(2):")
println(M2)

# m1 = 1 0 0 0
#      -3 1 0 0
#      -4 0 1 0
#      -2 0 0 1
#
# m2 = 1 0 0 0
#      0 1 0 0
#      0 -1 0 1
#
# What patterns do you observe in these products?
# M1 is a unit lower triangular matrix
# M2 is a 4x3 matrix which is close to a unit lower triangular matrix


#b
# Compute the inverse of each elementary row matrix
inv_M21 = inv(M21)
inv_M31 = inv(M31)
inv_M41 = inv(M41)

inv_M32 = inv(M32)
inv_M42 = inv(M42)
inv_M43 = inv(M43)

println("Inverse of M21:")
println(inv_M21)
println("Inverse of M31:")
println(inv_M31)
println("Inverse of M41:")
println(inv_M41)

println("Inverse of M32:")
println(inv_M32)
println("Inverse of M42:")
println(inv_M42)
println("Inverse of M43:")
println(inv_M43)


#c

# Compute U using the row operation sequence
U = M43 * M32 * M31 * M21 * A

println("Matrix U:")
println(U)

#d

# Compute L
L = inv_M21 * inv_M31 * inv_M32 * inv_M43

# L = 1 0 0
#    -.5 1 0
#    0 -.66 1
#
# What pattern do you observe in the matrix L?
# L is a lower triangluar unit matrix matrix

println("Matrix L:")
println(L)


#
#3.2.20
#

# Import LinearAlgebra for LU decomposition and permutation matrices
using LinearAlgebra

function solveAxb(A, b)
    # Check dimensions
    n, m = size(A)
    if n != m || n != length(b)
      error("Matrix must be square")
    end
    
    # LU decomposition with partial pivoting
    F, L, U = lu(A)
    x = zeros(n)
    
    # Forward substitution
    y = F \ b
    
    # Back substitution
    x = U \ y
    
    return x
end


A = [ 1 2 1 -1; 3 2 4 4; 4 4 3 4; 2 0 1 5]
b = [1, 2, 3, 4]

# Call solveAxb function
x = solveAxb(A, b)

# Display the solution
println("Solution x:")
println(x)


#
#3.3.3
#

function tridiaglu(A)
    n = size(A, 1)
    L = Matrix{Float64}(I, n, n)
    U = zeros(n, n)

    U[1, 1] = A[1, 1]
    for i in 2:n
        L[i, i-1] = A[i, i-1] / U[i-1, i-1]
        U[i-1, i] = A[i-1, i]
        U[i, i] = A[i, i] - L[i, i-1] * U[i-1, i]
    end
    return L, U
end

function bandedlu(A, p, q)
    n = size(A, 1)
    L = Matrix{Float64}(I, n, n)
    U = zeros(n, n)
    
    for i in 1:n
        for j in max(1, i-q):min(n, i+p)
            if i == j
                U[i, j] = A[i, j]
            elseif j < i
                L[i, j] = A[i, j] / U[j, j]
            else
                U[i, j] = A[i, j] - dot(L[i, max(1, j-q):i-1], U[max(1, j-q):i-1, j])
            end
        end
    end
    return L, U
end


# Define a tridiagonal matrix A
A_tridiag = [2.0 -1.0 0.0; -1.0 2.0 -1.0; 0.0 -1.0 2.0]

# Call tridiaglu function
L_tridiag, U_tridiag = tridiaglu(A_tridiag)

# Display results
println("LU Decomposition of the tridiagonal matrix A:")
println("L:")
println(L_tridiag)
println("U:")
println(U_tridiag)


# Define a banded matrix A
A_banded = [1.0 2.0 3.0 0.0; 4.0 5.0 6.0 7.0; 0.0 8.0 9.0 10.0; 0.0 0.0 11.0 12.0]

# Define the upper and lower bandwidths
p = 1
q = 1

# Call bandedlu function
L_banded, U_banded = bandedlu(A_banded, p, q)

# Display results
println("LU Decomposition of the banded matrix A:")
println("L:")
println(L_banded)
println("U:")
println(U_banded)

# Approximately how  many floating point operations does each function require
# 
# tridiaglu: 6n - 6, complexity O(n)
# bandedlu: 2n(p + q + 1)^2 , complexity O(n^2)
