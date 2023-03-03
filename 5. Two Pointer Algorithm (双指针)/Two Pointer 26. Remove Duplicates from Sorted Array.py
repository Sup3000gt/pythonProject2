class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 快慢指针
        slow = 1
        fast = 1
        n = len(nums)
        while fast < n: # 当快指针没有越界的时候
            if nums[fast] != nums[fast - 1]:    # 首先判定快指针指向的和之前的一位数是否不同，因为fast-1所以 快指针要从1开始
                nums[slow] = nums[fast]         # 如果不同用快指针的值替换掉慢指针的值
                slow += 1                       # 然后 慢指针右移
            fast += 1                           # 快指针 无论如何 每一次遍历都会右移一次
        return slow                             # 最后返回慢指针