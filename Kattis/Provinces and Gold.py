hands = input()
lst = hands.split(" ")      # After split, we will get a list with ["gold" , "Silver" , "Copper"]
BuyPower = int(lst[0]) * 3 + int(lst[1]) * 2 + int(lst[2]) * 1  # multiply by its worth to get Buypower
finalString = ""  # create a empty final statement
if BuyPower >= 8:  # check what victory cards can buy
    finalString += "Province"
elif 5 <= BuyPower < 8:
    finalString += "Duchy"
elif 2 <= BuyPower < 5:
    finalString += "Estate"
treasureCard = BuyPower
if treasureCard >= 6:  # check what treasure card can buy
    finalString += " or Gold"
elif treasureCard >= 3:
    finalString += " or Silver"
elif treasureCard >= 2:
    finalString += " or Copper"
else:
    finalString += "Copper"
print(finalString)  # return final String
