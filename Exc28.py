# get a username from the user. 3 rules must apply:
#   1. username can't have more than 12 chars.
#   2. usrname can't include any space.
#   3. username can't include any numbers.


username = input("Enter your name: ").capitalize()

if len(username) > 12:
    print("Username can't be more than 12 characters.")
elif not username.find(" ") == -1:
    print("Username can't contain any spaces.")
elif not username.isalpha():
    print("Username can't contain any numbers")
else:
    print(f"Welcome {username}.")
