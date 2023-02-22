class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针解法
        slow = 0  # 慢指针的计数器
        for fast in range(len(nums)):  # 用快指针遍历一次
            if nums[fast] != 0:        # 当快指针指到的不是0时，那么就把慢指针指向快指针
                nums[slow] = nums[fast]
                slow += 1              # 慢指针计数器+1
        for i in range(slow, len(nums)):    # 当快指针遍历结束之后，从计数器到数组的尾部都是0，用一个for循环 替换成 0
            nums[i] = 0