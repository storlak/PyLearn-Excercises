# while loop and how to escape from it
name = input("Enter your name: ")
while name == "":
    print("You did not enter your name.")
    name = input("Enter your name: ")
print(f"Hello {name}.")

num = int(input("Enter a number between 1-10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid.")
    num = int(input("Enter a number between 1-10: "))  # this is escape loop.

print(f"Your number is {num}.")
