def division(a, b):
    try:
        result = int(a / b)
        print(f"The result of {a} divided by {b} is {result}.")
    except ZeroDivisionError:
        print("Error, You can not divide by 0")
    except NameError:
        print("a and b must be numbers.")


division(8, 0)
