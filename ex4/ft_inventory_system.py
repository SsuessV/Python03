import sys

if __name__ == "__main__":
    inventory = {}
    print("=== Inventory System Analysis ===")
    if len(sys.argv) == 1:
        print("Usage: python3 ft_inventory_system.py <item:quantity>")
    else:
        for args in sys.argv[1:]:
            try:
                elements = args.split(":")
                if len(elements) != 2 or not elements[0]:
                    print(f"Error - invalid parameter '{args}'")
                    continue
                item_name = elements[0]
                quantity = int(elements[1])

                if quantity < 0:
                    print(f"Quantity error for '{item_name}'"
                          f": negative quantity")
                    continue

                if item_name in inventory:
                    print(f"Redundant item '{item_name}'- discarding")
                    continue
                inventory[item_name] = quantity
            except ValueError as e:
                print(f"Quantity error for '{item_name}': {e}")

        print(f"Got inventory: {inventory}")
        print(f"Item list: {list(inventory.keys())}")

        total_quantity = sum(inventory.values())
        print(f"Total quantity of the {len(inventory)} "
              f"items: {total_quantity}")

        if total_quantity > 0:
            for item in inventory:
                percentage = inventory[item] / total_quantity * 100
                print(f"Item {item} represents {percentage:.1f}%")

        if inventory:
            max_quantity = max(inventory.values())

            for item in inventory:
                if inventory[item] == max_quantity:
                    most_abundant = item
                    break
            print(f"Item most abundant: {most_abundant} "
                  f"with quantity {max_quantity}")

            min_quantity = min(inventory.values())
            for item in inventory:
                if inventory[item] == min_quantity:
                    least_abundant = item
                    break
            print(f"Item least abundant: "
                  f"{least_abundant} with quantity {min_quantity}")
        else:
            print("No items in inventory.")
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")
