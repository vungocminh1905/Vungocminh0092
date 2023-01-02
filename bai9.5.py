import math
A = lambda x,n: (math.pow(math.pow(x,2)+x+1,n)) + (math.pow(math.pow(x,2)-x+1,n))
print("A= ", A(3,4)) 