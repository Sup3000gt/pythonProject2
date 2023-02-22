class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        numSum = sum(nums) # 首先求数组的总和
        leftSum = 0 # 定义一个变量来计算左半边总和
        for i in range(len(nums)): # 开始遍历, 用总和 减去左边总和 再 减去 当前index的值, 就是右边的总和
            if numSum - leftSum - nums[i] == leftSum:   # 如果这时候右边总和 和 左边总和一样
                return i        # 那么返回当前的index值
            leftSum += nums[i]  # 不然把 当前的index的值加入到左边总和之后 开始下一次循环
        return -1               # 循环到结尾都没有左右相等的 返回-1