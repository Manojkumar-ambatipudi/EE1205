import numpy as np
import matplotlib.pyplot as plt

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

G_LP = 0.2545
num = G_LP

Omega_p1 = 0.443
Omega_p2 = 0.541

Omega_s1 = 0.421
Omega_s2 = 0.568

# Define parameters for transformation
B = 0.098
Omega0 = 0.483

# Perform transformation to get s_L
s_L = (1j * w)**2 + Omega0**2
s_L = s_L / (B * (1j * w))

# Band pass gain
G_bp = 1.0446

# Substitute s = jw into H(s)
H = G_bp * (num / np.polyval(den, s_L))

# Plot magnitude response for H(s)
plt.figure()
plt.plot(w, abs(H), linewidth=1)
plt.title('Band Pass Filter')
plt.xlabel('Analog Frequency ($\Omega$)')
plt.ylabel('|H_{a,BP}($\Omega$)|')
plt.grid(True)
plt.ylim(0, 1.4)
plt.savefig("../figs/Band_Pass_Filter.png")
