#Exc by Mosh: Converting lbs and kg.

weight = int(input("Enter your weight : "))
unit = input("(L)bs or (K)gs? ")

if unit.upper == "L":
    converted = weight * 0.45
    print(f"You're {converted} kgs.")
else: 
    converted = weight / 0.4589
    print(f"You're {converted} lbs.")
