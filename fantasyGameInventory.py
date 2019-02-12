# inventory.py chapter 5
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(k + '  :  ' + str(v))
        item_total += v
    print("Total number of items: " + str(item_total))


# displayInventory(stuff)
def addToInventory(inventory, addedItems):
    totalValue = 0
    for i in addedItems:
        val = inventory.setdefault(i, 1)  # return the corresponding value of the key i
        if val != 1:
            inventory[i] += 1
    for k, v in inventory.items():
        totalValue += v
    print("Total items in current inventory is: " + str(totalValue))
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
