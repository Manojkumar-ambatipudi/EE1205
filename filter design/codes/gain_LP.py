import numpy as np

# Given parameters
s1 = -0.1432 - 0.9864j
s2 = -0.3456 - 0.4086j
s3 = -0.3456 + 0.4086j
s4 = -0.1432 + 0.9864j
epsilon = 0.5
Omega_Lp = 1

# Generate the denominator polynomial
den = np.poly([s1, s2, s3, s4])
num = np.array([1])
s = 1j*1  # use Omega = 1
H = num / np.polyval(den, s)

req = 1 / np.sqrt(1 + epsilon**2)

Gain_LP = req / abs(H)
print(Gain_LP)
