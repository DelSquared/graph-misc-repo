import numpy as np
import sympy as sp
import math as m


#THIS SCRIPT IS STILL, FOR ALL INTENTS AND PURPOSES, UNDER CONSTRUCTION

def S(i, j):
    if (m.sqrt(i + j + 2) == m.floor(m.sqrt(i + j + 2))) and i!=j:
        return 1
    else:
        return 0

for n in range(2, 30):
    E=0
    AvgD=0
    minDeg=n
    maxDeg=0
    A = sp.Matrix(n, n, S)
    An = A**n
    #Diag=sp.Matrix.zeros(n, 1)
    #for i in range(0, n):
        #Diag[i,0]=An[i,i]
    #for i in range(0, n):
        #for j in range(0, n):
            #E+=A[i,j]/2
    #AvgD=sp.N(2 * E / n, 3)
    L,U,_=A.LUdecomposition()
    dA = sp.Matrix.det(A)
    dL = sp.Matrix.det(L)
    dU = sp.Matrix.det(U)
    #for i in range(0, n):
        #D=0
        #for j in range(0, n):
            #D += A[i, j]
        #if D<minDeg:
            #minDeg=D
        #if D>maxDeg:
            #maxDeg=D
    #x = sp.symbols('x')
    #I = np.identity(n)
    #C = (A - x * I)
    #P = sp.nsimplify(sp.expand(C.det()))
    #print(n,"vertices has: ",E,"\\\\")
    #print(n,"vertices has: ",E,",",minDeg,",",AvgD,",",maxDeg,"\\\\")
    #print('$',sp.latex(sp.sympify(P)),"$ \\\\\\\\")
    #print('$',sp.latex(sp.sympify(A)),"$ \\\\\\\\\\\\")
    #print('$',sp.latex(sp.sympify(Diag)),"$ \\\\\\\\\\\\")
    #print('$',sp.latex(sp.sympify(L)),sp.latex(sp.sympify(U)),"$ \\\\")
    print(dA, "=", dL, " ", dU)
