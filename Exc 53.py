# filter array that will return only even elements from the original array
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = []

for element in arr:
    if element % 2 == 0:
        filter_arr.append(element)
    elif element % 2 != 0:
        continue
    else:
        filter_arr.append(False)

new_arr = arr[filter_arr]

print(filter_arr)
print(new_arr)
