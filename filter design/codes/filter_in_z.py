import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = 0.4166*s**4/(10841.6578473394*s**8 + 1038.68286173278*s**7 + 10270.83605853*s**6 + 734.783982517724*s**5 + 3612.34316014149*s**4 + 171.417020497577*s**3 + 558.977491187382*s**2 + 13.1875995284982*s + 32.1123984017901)

# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


