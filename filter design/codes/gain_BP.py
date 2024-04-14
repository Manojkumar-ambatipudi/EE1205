import numpy as np

# Given parameters
s1 = -0.1432 - 0.9864j
s2 = -0.3456 - 0.4086j
s3 = -0.3456 + 0.4086j
s4 = -0.1432 + 0.9864j
epsilon = 0.5
Omega_Lp = 1

# Define denominator polynomial
den = np.poly([s1, s2, s3, s4])

# Define frequency range
w = np.arange(-2, 2.01, 0.01)

num = 0.2545

# Define parameters for transformation
B = 0.098
Omega0 = 0.483

# Perform transformation to get s_L
s_L = (1j * 0.443)**2 + Omega0**2
s_L /= B * (1j * 0.443)

H = num / np.polyval(den, s_L)
print(1 / abs(H))
