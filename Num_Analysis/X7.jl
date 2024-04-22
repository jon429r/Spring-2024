
using MatrixDepot
using LinearAlgebra

md = [4 1 -1; 2 7 1; 1 -3 12]
b1 = [19;3;31]


############Exploration 5.1.2####################

function jacobi(A, b, tol)
    # getting size and initalizing new x, error and iterations
    n = size(A, 1)
    x = zeros(n)
    x_new = zeros(n)
    iterations = 0
    error = tol + 1

    # While error is less than the threshold and iterations < 1000
        while error > tol && iterations < 1000
        for i in 1:n
            sum_term = 0.0
            for j in 1:n
                if j != i
                    # Sum of the products of the diagonal elements and the other elements of the row
                    sum_term += A[i, j] * x[j]
                end
            end
            # Jacobi formula
            x_new[i] = (b[i] - sum_term) / A[i, i]
        end

        # Calculate error
        error = norm(x_new - x)

        copyto!(x, x_new)

        iterations += 1
    end

    return x, iterations
end

n = length(md)
b = zeros(n) 
tol = 1e-6
elapsed_time = @elapsed begin
    x, iterations = jacobi(md, b1, tol)
end

println("Solution vector x (jacobi): ", x)
println("Number of iterations (jacobi): ", iterations)
println("Time elapsed: ", elapsed_time)

#####################################################

################Exploration 5.1.4###################
"""
Solve the linear system Ax = b by using the Jacobi method, where
A = [4 1 -1;
     2 7 1; 
    1 -3 12]
b = [19; 3; 31]

Compute the iteration matrix T = M^-1 * N using the fact that M = D and N = -(L+U) for the Jacobi method. Determine whether ρ(T) < 1 without computing the eigenvalues of T explicitly.

Solution:

diagonal matrix = [4 0 0;
                   0 7 0;
                   0 0 12]
lower matrix = [0 0 0;
                2 0 0;
                1 -3 0]

upper matrix = [0 1 -1;
                0 0 1;
                0 0 12]

The iteration T matrix is given by: T = M^-1 * N, where N = -(L + U)
N = -(L + U) = - [0 1 -1; 2 0 1; 1 -3 0]
T = M^-1 * N = [0 1/4 -1/4; 2/7 0 -1/7; 1/12 -1/4 0]
p(T) = The maximum absolute value the rows sums
p(T) = 3/7 which is less than 1

"""
####################################################

################Exploration 5.1.6###################

function gauss_seidel(A,b,tol)
    # getting size and initalizing new x, error and iterations
    n = size(A, 1)
    x = zeros(n)
    x_new = zeros(n)
    iterations = 0
    error = tol + 1

    while error > tol && iterations < 1000
        for i in 1:n
            sum1 = dot(A[i, 1:i-1], x_new[1:i-1])  
            sum2 = dot(A[i, i+1:n], x[i+1:n]) 
            x_new[i] = (b[i] - sum1 - sum2) / A[i, i] 
        end

        error = norm(x_new - x)

        copyto!(x, x_new)

        iterations += 1
    end

    return x, iterations
end

n = length(md)
b = zeros(n) 
tol = 1e-6
elapsed_time = @elapsed begin
    x, iterations = gauss_seidel(md, b1, tol)
end

println("Solution vector x (guass-seidel): ", x)
println("Number of iterations (guass-seidel): ", iterations)
println("Time elapsed: ", elapsed_time)


################################################

################Exploration 5.1.9###################

function SOR(A, b, w, tol)
    n = size(A, 1)
    x = zeros(n)
    x_new = similar(x)
    iterations = 0
    error = tol + 1

    while error > tol
        for i in 1:n
            sum1 = dot(A[i, 1:i-1], x_new[1:i-1])  
            sum2 = dot(A[i, i+1:end], x[i+1:end])  
            x_new[i] = (1 - w) * x[i] + (w / A[i, i]) * (b[i] - sum1 - sum2)  
        end

        error = norm(x_new - x)
        
        copyto!(x, x_new)

        iterations += 1
    end

    return x, iterations
end

b = [0;0;0]
tol = 1e-6

for w in 0.25:0.25:2.0
    println("Value for w ", w)
    elapsed_time = @elapsed begin
        x, iterations = SOR(md, b1, w, tol)
    end

    println("Solution vector x (SOR): ", x)
    println("Number of iterations (SOR): ", iterations)
    println("Elapsed time (SOR): ", elapsed_time)
end

######################################################

################Exploration 5.2.4###################

function steepest_descent(A, b, x0, tol)
    n = length(b)
    x = copy(x0)
    r = b - A * x
    iterations = 0
    
    while norm(r) > tol
        alpha = dot(r, r) / dot(A * r, r)  
        x += alpha * r 
        r = b - A * x  
        iterations += 1
    end
    
    return x, iterations
end

A1 = [2 1; 1 2]
A2 = [4 2; 2 1]

b1 =  [1; 2]
x0 = [0;0]

tol = 1e-6  
elapsed_time = @elapsed begin
    x_sd, iterations_sd = steepest_descent(A1, b1, x0, tol)
end

println("Solution vector x (Steepest Descent): ", x_sd)
println("Number of iterations (Steepest Descent): ", iterations_sd)
println("elapsed time (steepest_descent) ", elapsed_time)

elapsed_time = @elapsed begin
    x_sd, iterations_sd = steepest_descent(A2, b1, x0, tol)
end

println("Solution vector x (Steepest Descent): ", x_sd)
println("Number of iterations (Steepest Descent): ", iterations_sd)
println("elapsed time (steepest_descent) ", elapsed_time)

#######################################################


