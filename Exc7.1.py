phone = input("Phone: ")

output = ""

for char in phone:
    if char.isdigit():
        digit_word = [
            "zero",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ][int(char)]
        output += digit_word + " "
    else:
        output += "!"  # Handle non-numeric characters
print(output)
