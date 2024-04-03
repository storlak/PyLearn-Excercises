# basic calculator
operator = input("Enter an operator(+,-,*,/): ")
num1 = float(input("Enter a number: "))
num2 = float(input("Entera second number: "))
if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{operator} is not a valid operator!")
