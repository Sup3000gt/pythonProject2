user_writing = []                       # create a empty list to storage value for user input
while True:
    line = input()
    if line != "0":                     # if is not 0, add to list
        user_writing.append(line)
    else:
        break                           # if it is 0, stop

for number in user_writing:             # iterate the list
    n = list(number)                    # for each number, we change it to a list of numbers
    total = 0                           # set a total sum, then add each individual number in the list to get total sum
    for i in n:
        total += int(i)

    for p in range (11,101):            # the maximum number will be 100, so we just have to run a loop from 11 to 101
        new = p * int(number)           # start from 11, use each number * our original number in the list
        new = list(str(new))            # and set it to new, then we repeat everything we just did to find sum of digit
        total2 = 0
        for j in new:
            total2 += int(j)
        if total2 == total:             # if the sum of new number == the sum of digit of original number
            print(p)                    # return p , and break the loop
            break