# calculate the standart deviation of 8,9,10 and print the result

x1, x2, x3 = 10, 11, 9
mean = (x1 + x2 + x3) / 3.0
var = ((x1 - mean) ** 2 + (x2 - mean) ** 2 + (x3 - mean) ** 2) / 3.0
std = var ** (1 / 2)
print(f"The standard deviation: {std:.2f}")

# or
import math

# Given numbers
numbers = [8, 9, 10]

# Step 1: Calculate the mean
mean = sum(numbers) / len(numbers)

# Step 2: Calculate the deviations from the mean
deviations = [(x - mean) for x in numbers]

# Step 3: Square each deviation
squared_deviations = [d**2 for d in deviations]

# Step 4: Calculate the variance
variance = sum(squared_deviations) / len(numbers)

# Step 5: Calculate the standard deviation
standard_deviation = math.sqrt(variance)

print(standard_deviation)

# or

# Given numbers
numbers = [8, 9, 10]

# Step 1: Calculate the mean
mean = sum(numbers) / len(numbers)

# Step 2: Calculate the deviations from the mean
deviations = []
for x in numbers:
    deviations.append(x - mean)

# Step 3: Square each deviation
squared_deviations = []
for d in deviations:
    squared_deviations.append(d**2)

# Step 4: Calculate the variance
variance = sum(squared_deviations) / len(numbers)


# Step 5: Calculate the standard deviation (square root of the variance)
# Implementing the square root function manually
def sqrt(number, epsilon=1e-10):
    guess = number / 2.0
    while abs(guess * guess - number) > epsilon:
        guess = (guess + number / guess) / 2.0
    return guess


standard_deviation = sqrt(variance)

print(standard_deviation)
