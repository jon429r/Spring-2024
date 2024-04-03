
using LinearAlgebra

function find_singular_threshold()
    E = floatmin(Float64)  # Start with the smallest positive normal floating-point number
    while true
        try
            # Define the matrix A with the current value of E
            A = [1 1+E; 1-E 1]

            # Compute the LU decomposition of A
            F = lu(A)

            # Extract the upper triangular matrix U
            U = F.U

            # Check if U is singular
            if det(U) == 0
                println("Threshold reached: For E = $E, U is singular.")
                return E
            end
        catch ex
            println("Error: ", ex)
            println("Threshold reached: For E = $E, U is singular.")
            return E
        end
        # Increment E and continue
        E *= 2
    end
end

# Find the singular threshold
threshold = find_singular_threshold()

