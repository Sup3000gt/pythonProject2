a, b = input().split()
a = int(a)
b = int(b)
if b % a == 0:  # if the poffins and pokemon can evenly divided, then all pokemon will have equal poffins
    print(0)        # difference will be 0
else:
    print(1)        # else means poffins can't evenly distribute, some pokemon will have 1 more poffins
