import sys

inventory = {}
print("=== Inventory System Analysis ===")

for args in sys.argv[1:]:
    try:
        elements = args.split(":")
        if len(elements) != 2:
            print(f"Error- Invalid parameter '{args}'")
            continue
        item_name = elements[0]
        quantity = int(elements[1])
        if item_name in inventory:
            print(f"Redundant item '{item_name}'- discarding")
            continue
        inventory[item_name] = quantity
    except ValueError as e:
        print(f"Quantity error for '{item_name}': {e}")

print(f"Got inventory: {inventory}")
print(f"Item list: {list(inventory.keys())}")
print(f"Total quantity of the {len(inventory)}"
      "items: {sum(inventory.values())}")
for item in inventory:
    percentage = inventory[item] / sum(inventory.values()) * 100
    print(f"Item {item} represents {percentage:.1f}%")
    max_quantity = max(inventory.values())

for item in inventory:
    if inventory[item] == max_quantity:
        most_abundant = item
        break
print(f"Item most abundant: {most_abundant} with quantity {max_quantity}")
min_quantity = min(inventory.values())
for item in inventory:
    if inventory[item] == min_quantity:
        least_abundant = item
        break
print(f"Item least abundant: {least_abundant} with quantity {min_quantity}")
inventory["magic_item"] = 1
print(f"Updated inventory: {inventory}")
