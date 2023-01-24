class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # list MUST be sorted
        left = 0  # 左指针 等于0
        right = len(nums) - 1  # 右指针等于arr长度-1（因为0 index）
        answer = len(nums)
        while left <= right:  # 当左指针 比 右指针 小的情况下
            mid = (left + right) // 2  # 中间值 = (左指针的index+右指针的index) //2
            if nums[mid] < target:  # 如果中间值 < target， 左指针移到mid+1的位置，因为target必定在mid右边
                left = mid + 1
            elif nums[mid] >= target:  # 反之 右指针移动到mid-1的位置，因为target必定在mid左边
                right = mid - 1
                answer = mid
            else:
                return mid  # 如果以上2种情况都不是 那mid就是我们要找的target
        return answer  # 如果整个循环都结束，左右指针重叠了还没找到，说明target不在arr里面
