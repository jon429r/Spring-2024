#=
Exploration 3.1.6 Prove that the following row operations do not change the solution
set. Multiplying an equation by a scalar. Replacing equation i by the difference
of itself and a multiple of equation

modify to incorerate partial pivoting

return 1 matrix with [L\U]
and a vector p with permutation
=#

function gaussianElim(n)
  for j = 1, 2, ... , n − 1 do
      for i = j + 1, j + 2, . . . , n do 
          mij = aij/ajj 
          for k = j + 1, j + 2, . . . , n do 
            aik = aik − mijajk 
          end for
          bi = bi − mijbj
      end for 
  end for

end


