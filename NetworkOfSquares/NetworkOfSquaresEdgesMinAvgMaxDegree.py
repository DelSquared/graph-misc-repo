import numpy as np
import sympy as sp
import math as m

#This script runs the numerical method by default. Should the symbolic method be required, set the boolean to True.
#Note that the symbolic method is much less efficient to run so be sure to set the start and stop parameters accordingly
symbolic=False
start, stop = 2, 1000

def S(i, j): #defining rule for populating the adjacency matrix
  if (m.sqrt(i + j + 2) == m.floor(m.sqrt(i + j + 2))) and i!=j:
    return 1
  else:
    return 0

if symbolic==True: #symbolic method
  for n in range(start, stop):
    E=0
    AvgD=0
    minDeg=n-1
    maxDeg=0
    
    A = sp.Matrix(n, n, S) #defining adjacency matrix
    
    for i in range(0, n): #counting edges using Handshake Lemma
      for j in range(0, n):
        E+=A[i,j]/2
      
  AvgD=sp.N(2 * E / n, 3) #calculating average degree again using Handshake Lemma

  for i in range(0, n): #searching for min and max degree
    D=0
    for j in range(0, n):
      D += A[i, j]
    if D<minDeg:
      minDeg=D
    if D>maxDeg:
      maxDeg=D
    print(n,"vertices has: ",E,",",minDeg,",",AvgD,",",maxDeg,"\\\\") #LaTeX ready output
    
else: #numerical method
  for n in range(start, stop):
    E = 0
    AvgD = 0
    minDeg = n -1
    maxDeg = 0
    
    A = np.empty([n, n]) #defining adjacency matrix
    for i in range(0, n):
        for j in range(0, n):
            A[i, j] = S(i, j)
            
    for i in range(0, n): #counting edges using Handshake Lemma
      for j in range(0, n):
        E+=A[i,j]/2
        
    AvgD=2 * E / n #calculating average degree again using Handshake Lemma
    
    for i in range(0, n): #searching for min and max degree
      D=0
      for j in range(0, n):
        D += A[i, j]
      if D<minDeg:
        minDeg=D
      if D>maxDeg:
        maxDeg=D
    print(n,"vertices has: ",E,",",minDeg,",",AvgD,",",maxDeg,"\\\\") #LaTeX ready output

    
