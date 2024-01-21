import matplotlib.pyplot as plt
import numpy as np

a = 1.5  
r = 2.0
start = -3
end = 8

n_values = np.arange(start, end + 1).astype(np.float32)
gp_values = a * r ** n_values
plt.stem(n_values, gp_values, basefmt='b-', linefmt='d-', markerfmt='ro')
plt.title('General Term of Geometric Progression')
plt.xlabel('n')
plt.ylabel('Term Value')
plt.grid(True)
plt.show()
