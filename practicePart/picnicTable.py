def printPicnic(itemsDict,leftWidth,rightWidth):
    print('PICNIC ITE'.center(leftWidth+rightWidth,'-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth,'.')+str(v).rjust(rightWidth))

picnicItems = {'sandwiches':4,'apples':12,'cups':4,'cookies':800}
printPicnic(picnicItems,12,5)
printPicnic(picnicItems,20,6)
printPicnic(picnicItems,10,5)

# output
"""
----PICNIC ITE---
sandwiches..    4
apples......   12
cups........    4
cookies.....  800
--------PICNIC ITE--------
sandwiches..........     4
apples..............    12
cups................     4
cookies.............   800
---PICNIC ITE--
sandwiches    4
apples....   12
cups......    4
cookies...  800
"""