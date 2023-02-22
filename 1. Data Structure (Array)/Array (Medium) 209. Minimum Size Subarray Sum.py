class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf") # 创建一个无限大的数
        sum = 0     # 左右指针之和
        i = 0       # 左指针起始的位置
        for j in range(len(nums)):  # 用右指针遍历一遍list
            sum += nums[j]          # 把右指针指过的每个数字加起来
            while sum >= target:    # 如果这个数字大于等于目标值
                res = min(res,j-i+1)    # j-i+1 是右指针减去左指针,+1是因为0 index,
                                        # 然后比较这个数字和res,如果这个数字小 就用这个数字取代res
                sum -= nums[i]          # 然后开始移动左指针，如果移动1格，还是大于target
                                        # 那么 i = i+1, 直到 sum小于taget，那么跳出循环 继续移动右指针
                i += 1
        return 0 if res == float("inf") else res    # 最后如果res等于无限，那么说明while循环没有执行过
                                                    # 代表整个for-loop跑完 sum也不够target返还 0， 不然的话返还res即可