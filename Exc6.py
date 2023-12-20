# finding highest number in the list?
numbers = [6, 9, 17, 29, 38, 72, 21]
highest = numbers[0]
for number in numbers:
    if number > highest:
        highest = number
print(highest)

numbers = [6, 9, 17, 29, 38, 72, 21]
highest = max(numbers)
print(highest)


