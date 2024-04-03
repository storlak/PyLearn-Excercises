# Construct two lists, one containing all the keys of both dictionaries, and one containing all the values of each
# dictionary. (It is OK for values or keys to be repeated in the lists).

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'d': 100, 'e': 200, 'f': 300}
d3 = {'f': 30, 'g': 40}

d1.update(d2)
d1.update(d3)
print(list(d1.keys()))
print(list(d1.values()))