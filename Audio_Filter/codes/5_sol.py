import numpy as np
import matplotlib.pyplot as plt


N = 14
m = np.arange(N)
g = (-1/2)**m

h1 = np.pad(g, (0,2), 'constant', constant_values=(0))
h2 = np.pad(g, (2,0), 'constant', constant_values=(0))
h = h1 + h2 

x_temp = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
x = np.pad(x_temp, (0,8), 'constant', constant_values=(0))

X = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
    for n in range(0,N):
        X[k] += x[n] * np.exp(-1j * 2 * np.pi * n * k / N)  # Answer of 5.1
H = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
    for n in range(0,N):
        H[k] += h[n] * np.exp(-1j * 2 * np.pi * n * k / N)  # Answer of 5.1

Y = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
    Y[k] = X[k] * H[k]  # Answer of 5.2

y = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
    for n in range(0,N):
        y[k] += Y[n] * np.exp(1j * 2 * np.pi * n * k / N)  # Answer of 5.3

y = np.real(y) / N

# plots
plt.stem(range(0,N), y, markerfmt='C0o')
plt.title("y(n) by DFT")
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()

plt.savefig('yn_by_dft.png')

