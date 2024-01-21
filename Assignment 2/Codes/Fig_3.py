import matplotlib.pyplot as plt
import numpy as np

a = 1.5  
r = 2
start = -3
end = 8

n_values = range(start, end + 1, 1)
gp_values = [a*r**n for n in n_values]
plt.stem(n_values, gp_values, basefmt='b-', linefmt='d-', markerfmt='ro')
plt.title('General Term of Geometric Progression')
plt.xlabel('n')
plt.ylabel('Term Value')
plt.grid(True)
plt.show()