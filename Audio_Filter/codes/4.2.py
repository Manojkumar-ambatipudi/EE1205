import numpy as np
import matplotlib.pyplot as plt

n = np.arange(10)
g = (-1/2)**n

h1 = np.pad(g, (0,2), 'constant', constant_values=(0))
h2 = np.pad(g, (2,0), 'constant', constant_values=(0))
plt.stem(np.arange(12), h1+h2)
plt.title('Filter Impulse Response')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()

plt.savefig('hn.png')

