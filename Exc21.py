try:
    age = int(input("Your age: "))
    income = 20000
    risk = income / age
    print(f"You're {age} years old.")
except ZeroDivisionError:
    print("Age can't be zero.")
except ValueError:
    print("Invalid Value. Rerun and input a valid value.")
