import numpy as np
import matplotlib.pyplot as plt

m = np.arange(14)
g = (-1/2)**m
h1 = np.pad(g, (0,2), 'constant', constant_values=(0))
h2 = np.pad(g, (2,0), 'constant', constant_values=(0))
h = h1 + h2

nh = len(h)
x = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
nx = len(x)
y = np.zeros(nx + nh - 1)
for k in range(0, nx + nh - 1):
    for n in range(0, nx):
        if k - n >= 0 and k - n < nh:
            y[k] += x[n] * h[k - n]

plt.stem(range(0, nx + nh - 1), y)
plt.title('Filter Output using Convolution')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.savefig('y_by_conv.png')

