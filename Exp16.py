# Write the python program to implement Feed forward neural Network 
import numpy as np
def sig(x):
    return 1 / (1 + np.exp(-x))
def d_sig(x):
    return x * (1 - x)
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])
Y = np.array([[0],
              [1],
              [1],
              [0]])
np.random.seed(1)
w1 = np.random.rand(2, 4)
w2 = np.random.rand(4, 1)
for _ in range(10000):
    h = sig(np.dot(X, w1))
    o = sig(np.dot(h, w2))
    e = Y - o
    d_o = e * d_sig(o)
    e_h = d_o.dot(w2.T)
    d_h = e_h * d_sig(h)
    w2 += h.T.dot(d_o)
    w1 += X.T.dot(d_h)
print("Output:")
print(np.round(o, 3))