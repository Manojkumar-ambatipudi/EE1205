import matplotlib.pyplot as plt
import numpy as np

def gp_general_term(a, r, n):
    if n>1:
        return a * (r ** (n - 1))
    else:
        return 0

def plot_gp_general_term(a, r, start, end):
    n_values = np.arange(start, end + 1, 1)
    gp_values = [gp_general_term(a, r, n) for n in n_values]

    plt.stem(n_values, gp_values, basefmt='b-', linefmt='r-', markerfmt='ro')
    plt.title('General Term of Geometric Progression')
    plt.xlabel('n')
    plt.ylabel('Term Value')
    plt.grid(True)
    plt.show()


a = 1.5  
r = 2
start_n = -6
end_n = 6

plot_gp_general_term(a, r, start_n, end_n)
