result = []
for number in range(1, 101):
    for n in range(2, 10):
        if number % n == 0:
            result.append(number)
            break

not_divisible = set(range(1, 100)) - set(result)
print(not_divisible)

# solution 2 comprehension
result = {number for number in range(1, 101) for n in range(2, 10) if number % n == 0}
result = set(range(1, 101)) - result
print(result)
