Tims = input().split(" ")       # split input into a list
totalEmpty = int(Tims[0]) + int(Tims[1])    # first two number equal or total bottle
recycle = int(Tims[2])                      # third number is recycle requirements

count = 0                                   # set a counter to count our

# 9 0 3
while totalEmpty >= recycle:                # while our empty bottle is > recycle keep looping
    newDrink = totalEmpty // recycle
    count += newDrink                       # keep update our count
    remainder = totalEmpty % recycle        # find out how many new drink we can recycle and reminder
    totalEmpty = newDrink + remainder       # update new total empty bottle going back loop
print(count)                                # return count
