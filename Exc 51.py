# using zip function
names = ["Tunta", "Kunta", "Evo", "Kazu"]
ages = [9, 15, 40, 46]
combined_data = zip(names, ages)
for name, age in combined_data:
    print(f"{name} is {age} years old.")
