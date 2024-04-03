# Write a function to find the average
# finding the average
def average(*args):
    sum_values = 0
    for value in args:
        sum_values += value
    return sum_values / len(args)


print(average(1, 2, 3))

# finding the average2 by fmean
from statistics import fmean

my_list = [1, 2, 3]
print(fmean(my_list))

# finding average using lambda
average = (lambda x: sum(x) / len(x))(my_list)
print(average)
