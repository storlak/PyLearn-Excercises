def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    if x != 0:
        return x / y
    else:
        return "Error. Division by zero"


def multiplie(x, y):
    return x * y


# user input
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

# getting the result
sum_result = add(num1, num2)
difference_result = subtract(num1, num2)
division_result = divide(num1, num2)
multiplication_result = multiplie(num1, num2)

print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Division: {division_result}")
print(f"Multiplication: {multiplication_result}")
