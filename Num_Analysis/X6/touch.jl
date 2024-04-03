using LinearAlgebra
using Plots

function create_matrix(n)
    sub_diag = ones(n-1)
    diag = -2 * ones(n)
    super_diag = ones(n-1)
    A = Tridiagonal(sub_diag, diag, super_diag)
    return A
end

function compute_condition_number_log2(A)
    println("Condition number: ", cond(A, 2))
    println("Condition number (log2): ", log2(cond(A, 2)))
    println("Condition number (log10): ", log10(cond(A, 2)))
end

function main()
    n_values = [7]  # For a 7x7 matrix

    for n in n_values
        A = create_matrix(n)
        compute_condition_number_log2(A)
    end
end

main()

