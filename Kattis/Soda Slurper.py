Tims = input()
Tims = Tims.split(" ")
totalEmpty = int(Tims[0]) + int(Tims[1])
recycle = int(Tims[2])


# 9 0 3
def drink(Empty,recycle):
    newDrink = Empty // recycle
    remainder = Empty % recycle
    if newDrink + remainder < recycle:
        return 0
    else:
        newDrink += drink(newDrink + remainder,recycle)
    return newDrink

print(drink(totalEmpty,recycle))
