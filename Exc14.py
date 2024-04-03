# check if income is sufficient for buying a house. use if else statement
# see the difference between me and chatgpt

# This is my code
good_credit = True
house = 1000_000

if good_credit:
    down_payement = int(house * 0.1)
else:
    down_payement = int(house * 0.2)
print(f"Down Payment is ${down_payement}")

# This is by ChatGPT
good_credit = True
house = 1000000

down_payment_percentage = 0.1 if good_credit else 0.2
down_payment = int(house * down_payment_percentage)

print(f"Down Payment is ${down_payment}")
