# Checking Credit Card validity
# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
#        (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid


sum_odd_digits = 0
sum_even_digits = 0
total = 0

# step 1
card_number = input("Enter a card number: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]
# step 2
for x in card_number[::2]:
    sum_odd_digits += int(x)
# step 3
for x in card_number[1::2]:
    x = int(x * 2)
    if x >= 10:
        sum_even_digits += 1 + (x % 10)
    else:
        sum_even_digits += x
# step 4
total = sum_even_digits + sum_odd_digits
# step 5
if total % 10 == 0:
    print("VALID CREDIT NUMBER")
else:
    print("INVALID CREDIT CARD NUMBER")
