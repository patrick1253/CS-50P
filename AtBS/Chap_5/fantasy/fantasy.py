# AtBS assignment: Chap 5: create an inventory for a fanatasy game using dictionaries.

# I have tweaked it a bit by adding additional functionality to update the inventory
# on the fly.  However, the inventory dict is not persistent and re-sets every time 
# the program is re-started.

import pprint

inventory = {'arrows': 12, 'gold coins': 42, 'ropes': 1, 'torches': 2, 'daggers': 1 }

def main():
    updateInventory()
    displayInventory()
    #pprint.pprint(inventory)


def updateInventory():
    loot = {}

    while True:
        try:
            item = input("Item you looted (^C to exit): ")
            qty = int(input(f"Number of {item}: "))
            loot.update({item: qty})
            inventory.setdefault(item, 0)
        except KeyboardInterrupt:
            break

    for item, qty in loot.items():
        if item in inventory.keys():
            v = inventory[item]
            inventory.update({item: v + qty})


def displayInventory():
    total_items = 0
    print("\nItems on Hand:")

    for k, v in inventory.items():
        print(f"{k}: {v}")
        total_items = total_items + v

    print(f"\nTotal number of items: {total_items}\n")
    

if __name__ == "__main__":
    main()
