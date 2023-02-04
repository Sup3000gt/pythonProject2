num = input()
number = input()
lst = number.split(" ")
expense = 0
income = 0
for i in lst:
    if int(i) < 0:
        expense -= int(i)
    else:
        income += int(i)
if income >= expense:
    print(expense)
else:
    print(income)