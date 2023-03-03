class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 解法1 把整个大整数join到一起然后变成int 之后+1 再变回list形态
        # res = "".join(str(i) for i in digits)
        # res = str(int(res)+1)
        # lst = []
        # for character in res:
        #     lst.append(int(character))
        # return lst

        # 解法2
        # 从最低位开始做加法运算
        for i in range(len(digits)- 1, -1, -1):             # 从列表的最后一位开始到0，步长-1
            if digits[i] != 9:                              # 如果不是 哪一位不是9,就把那个数字直接+1
                digits[i] += 1
                for j in range(i + 1, len(digits)):         # 然后从那一位后面的一位数开始到n的结尾
                    digits[j] = 0                           # 全部都变成 0
                return digits                               # 最后返还 大整数的数组

        # 如果上述步骤 全部都没返回任何东西 那么只有一种情况
        # digits 中所有的元素均为 9 例如 [9,9,9,9,9,9]
        # 这种情况 我们直接返回 长度为len(digits)的数组 然后全部为0 再在前面+1
        return [1] + [0] * len(digits)                    