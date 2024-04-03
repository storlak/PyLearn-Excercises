# Example 1: Filter even numbers from a list using lambda
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_newList = list(filter(lambda x: x % 2 == 0, myList))
print(my_newList)

# Example 2: Filter positive numbers from a list using lambda
numbers = [-2, -1, 0, 1, 2, 3, 4, 5]
numbers2 = list(filter(lambda x: x > 0, numbers))
print(numbers2)

# Example 3: Filter strings with length greater than 3
words = ["apple", "banana", "cat", "dog", "elephant"]
longer_words = list(filter(lambda x: len(x) > 3, words))
print(longer_words)
