import numpy as np
import sympy as sp
import math as m

#Note: This code is very computationally intensive due to the symbollic nature of the code. Remember to tweak the
#start and stop parameters to your liking.

start, stop = 1, 50 #search range
p=False

def S(i, j): #Function That defined the rule for populating the adjacency matrix
  if (m.sqrt(i + j + 2) == m.floor(m.sqrt(i + j + 2))) and i!=j:
    return 1
  else:
    return 0
    

if p==False:
  for n in range(start, stop):
    A = sp.Matrix(n, n, S) #populating the adjacency matrix
    x = sp.symbols(’x’) #placeholder for characteristic polynomial
    I = np.identity(n) #identity matrix (self explanatory)
    C = (A - x * I) #definition of characteristic polynomial
  
    P = sp.nsimplify(sp.expand(C.det())) #symbolic simplification
    print(’$’,sp.latex(sp.sympify(P)),"$ \\\\\\\\") #output is given in latex code ready to be copied to a latex document
else:
  for n in range(2, 21):
    A = sp.Matrix(n, n, S) #populating the adjacency matrix
    An = A**n #raising A to the nth power 
    x = sp.symbols(’x’) #placeholder for characteristic polynomial
    I = np.identity(n) #identity matrix (self explanatory)
    C = (An - x * I) #definition of characteristic polynomial
    
    P = sp.nsimplify(sp.expand(C.det())) #symbolic simplification
    print(’$’,sp.latex(sp.sympify(P)),"$ \\\\\\\\") #output is given in latex code ready to be copied to a latex document
