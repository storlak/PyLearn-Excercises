# check the customer information
customer = {"name": "John Smith", "age": 30, "is_verified": True}
customer["birthday"] = "1 April 1977"
print(customer["birthday"])

print(id(customer))  # we can use this also for comparing variables.

data1 = {"Zoltana": 37}
data2 = data1
data2["Selenga"] = 25
print(id(data1) == id(data2))
