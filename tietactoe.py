
"""
board  = { "TopL" : ' ', 'TopM' :' ',"TopR":' ',
            "ML" : ' ', 'MM':' ', "MR":' ',
            "BL" : ' ', 'BM':' ',"BR":' '
}
print(board)

"""

def displayInventory(inventory):
    import pprint
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v
        print(v,'  ',k.upper())
    print("Total number of items: " + str(item_total))


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
import pprint
pprint.pprint(stuff)
displayInventory(stuff)
