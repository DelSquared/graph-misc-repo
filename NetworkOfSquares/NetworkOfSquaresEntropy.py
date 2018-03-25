import numpy as np
from matplotlib import pyplot as plt

#This script explores a function of the degrees of vertices of a graph G: F(G)=SUM(ln(dv)/dv) where dv=deg(v). It is referred to as an
#"Entropy" because by making a change of variables p=1/dv, we get F(G)=-SUM(p ln(p)) which is effectively the Shannon Entropy. Some
#ready made plots and results can be found as PNG and CSV files along with this script up to graphs on 1000 vertices for the "sum of
#pairs adding to squares" conjecture by Matt Parker. This script mainly tries to generate a statistic for small cases of such a graph
#not an attempt to prove the conjecture.

n = 100 #Number of vertices

H=np.zeros((n)) #List of the "entropies"

#Function to generate the adjacency matrix of a graph based on some rule.
def G(n):
    B = np.zeros((n, n))
    for i in range(n):
        for j in range(i):
            if np.round(np.sqrt(i + j + 2)) == np.sqrt(i + j + 2) and i != j:
                B[i, j] = 1
                B[j, i] = 1
    return B

#Function to calculate the "entropies". Care was taken to navigate around divergences that could occur when a zero could slide
#to the denominator
def S(g):
    s = 0
    k = g.shape[0]
    for i in range(k):
        w = 0
        for j in range(k):
            if g[i, j] != 0:
                w += g[i, j]
        if w != 0:
            s += np.log(w) / w
    return s

#Loop calculating the "entropies"
for _ in range(n):
    g = G(_)
    H[_]=S(g)
    if _%100==0:
        print ("current size being checked: ",_)

#Output to CSV
np.savetxt("Graph Entropy-like functional up to {} vertices.csv".format(n),H,fmt = '%f' ,delimiter=',')

#Plots
plt.plot(H)
plt.show()
