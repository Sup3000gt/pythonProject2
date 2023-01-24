# 1、首先，在 nums 数组中二分查找 target；
# 2、如果二分查找失败，则 binarySearch 返回 -1，表明 nums 中没有 target。此时，searchRange 直接返回 {-1, -1}；
# 3、如果二分查找成功，则 binarySearch 返回 nums 中值为 target 的一个下标。然后，通过左右滑动指针，来找到符合题意的区间
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums: List[int], target: int) -> int:  # 常规二分查找
            left, right = 0, len(nums) - 1
            while left <= right:  # 不变量：左闭右闭区间
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle - 1
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    return middle
            return -1

        index = binarySearch(nums, target)
        # 情况1：
        # 二分查找返回-1 说明 nums 中不存在 target，直接返回 [-1, -1]
        if index == -1: return [-1, -1]
        # 情况2：
        # nums 中存在 targe，则左右滑动指针，来找到符合题意的区间
        left, right = index, index  # 把左右指针都设置为当前二分查找返回的index
        # 向左滑动，找左边界
        # 左指针-1 要大于Index[0], 并且nums[左指针] 要等于 target，那么左指针-1 继续往左移动
        while left - 1 >= 0 and nums[left - 1] == target: left -= 1
        # 向右滑动，找右边界
        # 右指针+1 要小于列表的长度, 并且nums[右指针] 要等于 target，那么右指针+1 继续往右移动
        while right + 1 < len(nums) and nums[right + 1] == target: right += 1
        return [left, right]  # 最后返回 符合标准的左右指针
