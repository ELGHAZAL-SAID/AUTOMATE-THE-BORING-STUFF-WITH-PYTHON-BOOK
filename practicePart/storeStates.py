storcontity = {
                'firstType':{'apples':23,'Tv':49,'potatos':42,'onion':33},
                'secondType':{'laptop':93,'tea':32,'cofy':39,'apples':32},
                'thirdType':{'chears':33,'tables':99,'potatos':39,"Tv":39,'laptop':39},
                }



def totalItems(items,itemName):
    totalItems = 0
    for k , v in items.items():
        totalItems = totalItems + v.get(itemName,0)
    return totalItems


def showStatistics():
    print('apples :          ',totalItems(storcontity,'apples'))
    print('Tv     :          ',totalItems(storcontity,'Tv'))
    print('tea    :          ',totalItems(storcontity,'tea'))
    print('chears :          ',totalItems(storcontity,'chears'))
    print('onion  :          ',totalItems(storcontity,'onion'))
    print('cofy   :          ',totalItems(storcontity,'cofy'))
    print('tomatos:          ',totalItems(storcontity,'tomatos'))
    print('tables :          ',totalItems(storcontity,'tables'))
    print('potatos:          ',totalItems(storcontity,'potatos'))
    print('cars   :          ',totalItems(storcontity,'cars'))


showStatistics()
