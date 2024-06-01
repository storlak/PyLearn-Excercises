# Calculate the geometric mean of the following numbers: 4, 3, 4.5, 5 and print result to the console:
x1, x2, x3, x4 = 4, 3, 4.5, 5
geo = (x1 * x2 * x3 * x4) ** (1 / 4)
print(f"Geometric mean: {geo:.2f}")

# or

import math

x1, x2, x3, x4 = 4, 3, 4.5, 5
geo = math.pow(x1 * x2 * x3 * x4, 1 / 4)
print(f"Geometric mean: {geo:.2f}")

# or

import statistics

x1, x2, x3, x4 = 4, 3, 4.5, 5
geo = statistics.geometric_mean([x1, x2, x3, x4])
print(f"Geometric mean: {geo:.2f}")
