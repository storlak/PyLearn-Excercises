# finding even numbers in the list
data = list(range(1, 10))


def is_even(n):
    return n % 2 == 0


evens = [n for n in data if is_even(n)]
print(evens)
