# Exc by Mosh: Converting lbs and kg.

weight = int(input("Enter your weight : "))
unit = input("(L)bs or (K)gs? ")

if unit.upper == "L":
    converted = weight * 0.45
    print(f"You're {round(converted,1)} kgs.")
else:
    converted = weight / 0.4589
    print(f"You're {round(converted,1)} lbs.")
