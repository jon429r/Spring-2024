## X1 Due Feb 1 2024
## Explorations: 1.2.2,  1.2.5,   1.2.6,  1.2.13,  1.2.16


## 1.2.2 #################################################

A = [2 -4
    3 -5
    7 0]

B = [-5 1 4
    4 6 8
    10 5 0]

C = [-8 0
    2 -3
    -1 4]

BC = B*C
matrix1 = A + 3*BC

println("Resulting matrix 1: ")
println(matrix1)

## 1.2.5 #################################################

matrix2 = ones(3, 2)

println("Resulting matrix 2: ")
println(matrix2)

## 1.2.6 #################################################

matrix3 = 0:0.01:1
matrix3 = hcat(collect(matrix3))
println("Resulting matrix 3")
println(matrix3)

## 1.2.13 ################################################

x = rand(-10:10, 10)
logical_vector = (-1 .<= x) .& (x .<= 1)
println("Random Column Vector x:")
println(x)


println("Logical Column Vector:")
println(logical_vector)


## 1.2.16 ################################################


x = rand(-10:10, 10)

println("Vector x is:")
println(x)

MaxX = x[1]
MaxI = 1

for i in 2:10
    if x[i] > MaxX
        MaxX = x[i]
        MaxI = 1
    end
end

println("The max of x is: ", MaxX)
println("The index imax is: ", MaxI = 1)