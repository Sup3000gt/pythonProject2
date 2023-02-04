A = input()
case = input()
count = 0
my_list = case.split(" ")
for number in my_list:
    if int(number) < 0:
        count += 1
print(count)