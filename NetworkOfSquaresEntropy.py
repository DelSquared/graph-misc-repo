import numpy as np
from matplotlib import pyplot as plt

n = 1000

H=np.zeros((n))


def G(n):
    B = np.zeros((n, n))
    for i in range(n):
        for j in range(i):
            if np.round(np.sqrt(i + j + 2)) == np.sqrt(i + j + 2) and i != j:
                B[i, j] = 1
                B[j, i] = 1
    return B


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


for _ in range(n):
    g = G(_)
    H[_]=S(g)
    if _%100==0:
        print (_)

np.savetxt("Graph Entropy-like functional up to 1000 vertices.csv",H,fmt = '%f' ,delimiter=',')


# plt.plot(H)
# plt.show()