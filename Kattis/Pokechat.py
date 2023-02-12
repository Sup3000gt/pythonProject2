String = input()
code = input()

chunks = [code[i:i + 3] for i in range(0, len(code), 3)]  # loop entire code and split into multiple chunks of three
# for string  "001004006008" will split into, [001,004,006,008]

int_list = [int(x) for x in chunks]  # convert entire list into integer
result = ""
for number in int_list:  # loop entire  int_list, and use the value of integer as index of String
    result += String[number - 1]  # we need -1 because 0 index, then we join the list as string
print(result)
