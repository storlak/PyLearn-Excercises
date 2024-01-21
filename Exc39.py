# Concession stand

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25,
}
cart = []
total = 0
sorted_menu = dict(sorted(menu.items()))

print("--------MENU--------")
for key, value in sorted_menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif sorted_menu.get(food) is not None:  # if an item is not in the menu
        cart.append(food)
print("------YOUR CART------")
for food in cart:
    total += sorted_menu.get(food)
    print(food, end=" ")
print()
print(f"Total is ${total:.2f}.")
