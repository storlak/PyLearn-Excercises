def perform_operation(x, y):
    """
    Perform a mathematical operation using the parameters x and y.
    The function handles ZeroDivisionError and ValueError exceptions.
    """
    try:
        result = x / y
        value = int(input("Enter a number: "))
        print(f"Result: {result}, Input value: {value}")
    except ZeroDivisionError:
        print("You can not divide by 0")
    except ValueError:
        print("Invalid value. Enter a valid value.")


perform_operation(10, 9)
