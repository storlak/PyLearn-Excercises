# for loop to find even numbers
numbers = [88, 78, 56, 65, 91, 67, 31]
for number in numbers:
    if number % 2 == 0:
        print(number)

# using lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
