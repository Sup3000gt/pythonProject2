class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 解法1： hashMap 但是因为空间复杂度是O(n) 不符合题目
        # hashMap = {}        # make a new hash map
        # for i in range(len(nums)):  # if not seen , add to the map else increase the count by 1
        #     if nums[i] in dict1:
        #         hashMap[nums[i]] += 1
        #     else:
        #         hashMap[nums[i]] = 1
        # for key, val in hashMap.items():    # iterate the map see which value equal to 1
        #     if val == 1:                    # return it's key
        #         return key

        # 解法2 异或
        res = 0         # 初始化
        for n in nums:  # 对数组中的每一个数字进行 异或 XOR 操作
            res ^= n    # 一个数和 0 做 XOR 运算等于本身：a⊕0 = a
        return res      # 一个数和其本身做 XOR 运算等于 0：a⊕a = 0
                        # XOR 运算满足交换律和结合律：a⊕b⊕a = (a⊕a)⊕b = 0⊕b = b
                        # 因为这道题 只有一个数字只出现过1次,所以出现2次的数字全部变为0
                        # 最后 res = 只出现过一次的数字⊕0 等于只出现过一次的数字

