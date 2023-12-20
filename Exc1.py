name = "Serdar"

if len(name) < 3:
    print("Name must have min 3 chars")
elif len(name) > 50:
    print("Name can have max 50 chars")
else:
    print("Name looks good.")

# bu da chagpt kısa yazılış
name = "Serdar"
length = len(name)

if 3 <= length <= 50:
    print("Name looks good.")
else:
    print("Name must have between 3 and 50 characters.")

# buda Bard
name = "Serdar"
print("Name looks good.") if 3 <= len(name) <= 50 else print(
    "Name must have min 3 and max 50 chars"
)
