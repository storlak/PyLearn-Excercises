# make write a phone number in words

phone = input("Phone: ")
phone_numbers = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

output = ""

for chr in phone:
    output += phone_numbers.get(chr, "!") + " "
print(output)
