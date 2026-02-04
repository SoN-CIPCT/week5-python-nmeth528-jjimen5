# List Exercise

# 1. Create a list that contains 6 items
items = ["item1", "item2", "item3", "item4", "item5", "item6"]

# 2. Print the items in the list to the output console
for item in items:
    print(item)

# 3. Print the first two items using a slice
print(f"The first two items in the list are: {items[0]}, {items[1]}")

# 4. Print the middle two items using a slice
print(f"The middle two items in the list are: {items[2]}, {items[3]}")

# 5. Print the first and last items using indexes
print(f"The first and last items in the list are: {items[0]}, {items[-1]}")

# -------------------
# Tuple Exercise
# -------------------
# 1. A restaurant only offers five basic foods on its menu
menu = ("burger", "fries", "chicken tenders", "tacos", "pizza")
# 2. Print each item on the menu using a for loop
for food in menu:
    print(food)
# 3. Copy the tuple replacing two of the foods
revised_menu = ("burger", "fries", "soup", "sushi", "pizza")
# 4. Print each item on the revised menu using a loop
for food in revised_menu:
    print(food)