# format specifiers, flags
price1 = 3.12458
price2 = -9678.45
price3 = 12.34
price4 = 17.345
price5 = 17578900.345
price6 = 28000.90649587


print(f"Price1 is {price1:.2f}")  # shows 2 decimals.
print(f"Price2 is {price2:10}")  # adds 10 spaces.
print(f"Price3 is {price3:<10}")  # justifies to left. > justifies to right. ^ centers.
print(f"Price4 is {price4:+}")  # shows plus sign befor the number or-
print(f"Price5 is {price5:,}")  # thousand seperator.
print(f"Price6 is {price6:+,.2f}")  # all in one together.
