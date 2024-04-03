# show the username and domain name seperatly
email = input("Enter your email: ")
index = email.index("@")

username = email[0:index]
domain = email[index + 1 :]
print(f"Your username is {username} and domain name is {domain}.")
