import math

def solve_quadratic(a,b,c):
  z = b * b - 4 * a * c
  sqrt_z = math.sqrt(abs(z))

  if z > 0:
       x1 = (-b + sqrt_z) / (2*a) 
       x2 = (-b - sqrt_z) / (2*a) 
       return print(x1,x2)
  elif z == 0:
      x = (-b / (2 * a)) 
      return print(x)
  else:
      return print("No solution")
     
      


solve_quadratic(1,-5,6)
solve_quadratic(1,4,4)
solve_quadratic(1,0,1)


 
 
 