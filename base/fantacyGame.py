stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger','rope', 'gold coin', 'gold coin','rope', 'ruby','rope','hours','gold coin', 'dagger','rope', 'gold coin', 'gold coin','rope', 'ruby','rope','hours']


def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] not in inventory.keys():
            inventory.setdefault(addedItems[i],0)
            inventory[addedItems[i]] += 1
            
        elif addedItems[i] in inventory.keys():
            inventory[addedItems[i]] += 1
    return inventory

def displayInventory(inventory,rightWidth,leftWidth):
    print('Inventory'.center(rightWidth+leftWidth,'*'))
    totalItems = 0
    for key, value in inventory.items():
        totalItems = totalItems + value
        print(key.ljust(leftWidth,'-')+str(value).rjust(rightWidth,'-'))
    print("Total Items".ljust(leftWidth,'-'),str(totalItems).rjust(rightWidth,'-') )

staff = addToInventory(stuff,dragonLoot)
displayInventory(stuff,16,4)
