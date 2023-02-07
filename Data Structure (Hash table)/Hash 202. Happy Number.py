class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(num):     # 写一个函数来求 和
            total = 0       # 和 等于 零
            while num:      # 当这个数不等于零的时候 假设 19
                total += (num % 10)**2      #  9 % 10 = 9^2 = 81 ，把81加入到和里
                num = num//10               # 然后 19 = 19//10 = 1 然后把1加入到和里 变成82
            return total                    # 然后返回82
        record = set()                      # 创建一个空的set
        while True:                         # 无限循环到出结果
            n = happy(n)
            if n == 1:                      # 如果n变成1了 说明是快乐数， 返回True
                return True

            if n in record:
                return False
            else:
                record.add(n)               # 如果不是1 那么就把这个和加入到set里面, 如果下次再遇到这个数字 说明进入死循环
                                            # 返回错误值
