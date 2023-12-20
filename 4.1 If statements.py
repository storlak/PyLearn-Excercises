# bu benim yazdığım. aşağıda chatgptnin yazdığı var
good_credit = True
house = 1000_000

if good_credit:
    down_payement = int(house * 0.1)
else:
    down_payement = int(house * 0.2)
print(f"Down Payment is ${down_payement}")

# bunu chatgpt yazdı. ternary operator!
good_credit = True
house = 1000000

down_payment_percentage = 0.1 if good_credit else 0.2
down_payment = int(house * down_payment_percentage)

print(f"Down Payment is ${down_payment}")
