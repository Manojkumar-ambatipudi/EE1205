import numpy as np
import matplotlib.pyplot as plt
c = np.loadtxt("data.dat", delimiter='\t')

plt.stem(c[:, 0], c[:, 1])
plt.title("Plot of x(n) function")
plt.grid(1)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.savefig('fig_0.jpg')

plt.clf()
plt.stem(c[:, 0], c[:, 2])
plt.stem([12], [45.5], 'ro', basefmt='k', label='$x_1(k_1)$')
plt.title("Plot of x(n) function")
plt.grid(1)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.savefig('fig_1.jpg')



