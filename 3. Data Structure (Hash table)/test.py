def happy(num):  # 写一个函数来求 和
    total = 0  # 和 等于 零
    while num:  # 当这个数不等于零的时候 假设 19
        total += (num % 10) ** 2  # 9 % 10 = 9^2 = 81 ，把81加入到和里
        num = num // 10  # 然后 19 = 19//10 = 1 然后把1加入到和里 变成82
    return total






















