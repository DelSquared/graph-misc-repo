import numpy as np
import math as m
from matplotlib import pyplot as plt

N=50

def S(i, j):
    if (m.sqrt(i + j + 2) == m.floor(m.sqrt(i + j + 2))) and i != j:
        return 1
    else:
        return 0
#EArray=np.empty([N])
freq=np.zeros([N,N])

for n in range(2, N):
    E = 0
    AvgD = 0
    minDeg = n
    maxDeg = 0
    A = np.empty([n, n])
    for i in range(0, n):
        for j in range(0, n):
            A[i, j] = S(i, j)

    #for i in range(0, n):
        #for j in range(0, n):
            #E += A[i, j] / 2
    AvgD = np.round(2 * E / n, 2)
    #EArray[n]=E
    for i in range(0, n):
        for j in range(0, n):
            D=0
            D+=A[i, j]

        freq[n, int(D)] += 1/n

    #for i in range(0, n):
        #D = 0
        #for j in range(0, n):
            #D += A[i, j]
        #if D < minDeg:
            #minDeg = D
        #if D > maxDeg:
            #maxDeg = D

    #print(n, "vertices has: ", E, ",", minDeg, ",", AvgD, ",", maxDeg, "\\\\")
    # the histogram of the data
    plt.plot(freq[n,:])

#plt.plot(EArray)
#plt.xlabel("V")
#plt.ylabel("E")
#plt.show()




plt.xlabel('degrees')
plt.ylabel('%')
plt.grid(True)
plt.show()