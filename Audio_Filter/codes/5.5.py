import numpy as np
from numpy.fft import fft, ifft
import matplotlib.pyplot as plt

N = 14
m = np.arange(N)
g = (-1/2)**m
h1 = np.pad(g, (0,2), 'constant', constant_values=(0,0))
h2 = np.pad(g, (2,0), 'constant', constant_values=(0,0))
h = h1 + h2
x_temp = np.array([1.0,2.0,3.0,4.0,2.0,1.0])
x = np.pad(x_temp, (0,10), 'constant', constant_values=(0))
dftmtx = fft(np.eye(len(x)))
X = x @ dftmtx
H = h @ dftmtx
Y = H * X
invmtx = np.linalg.inv(dftmtx)
y = (Y @ invmtx).real

plt.stem(range(0,16), y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.savefig('yn_DFT_matrix.png')

