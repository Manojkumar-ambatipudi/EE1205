import numpy as np
import matplotlib.pyplot as plt

X = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
Y = np.loadtxt('y_n_output.txt', dtype='double')

plt.subplot(2, 1, 1)
plt.stem(range(0, 6), X)
plt.ylabel('$X(n)$')
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(range(0, 20), Y) 
plt.xlabel('$n$')
plt.ylabel('$Y(n)$')
plt.grid()

plt.savefig("Plot_Xn_Yn.png")

