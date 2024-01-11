def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Can not divide by 0"


while True:
    # getting user info
    operator = input("Enter an operator(+,-,*,/): ")
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter a second number: "))

    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    else:
        print("Invalid operator")
        continue
    print(f"Result:{result}")
