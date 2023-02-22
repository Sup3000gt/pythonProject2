class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # 解法1： 暴力破解
        if len(arr) < 3:  # 如果长度小于3 无法形成山峰 返回错误
            return False
        peek = max(arr)  # 数组里面的最大值还有最大值的index
        maxIndex = arr.index(peek)
        if peek == arr[-1] or peek == arr[0]:  # 如果最大值等于数组的第一个或者最后一位 那肯定无法形成山峰，因为山峰最高点一定在中间
            return False
        for i in range(maxIndex):  # 判定从0到最大值 也就是山峰的左侧，是否每一个数字都比前一个数字大，如果不是返回错误值
            if arr[i + 1] <= arr[i]:
                return False
        for i in range(maxIndex, len(arr) - 1):  # 从最大值判定到最后，也就是山峰的右侧，是否递减，如果不是 返回错误值
            if arr[i + 1] >= arr[i]:
                return False
        return True  # 如果都没返回错误值 说明是山峰，返回正确值
                        # Time comp O(n)

    class Solution:
        def validMountainArray(self, arr: List[int]) -> bool:
            # 解法2： 双指针
            # 左指针往右移动， 右指针往左移动，如果左右指针在中间相聚 那说明是山峰
            left = 0  # 建立左右指针
            right = len(arr) - 1
            if len(arr) < 3:  # 如果长度小于3 无法形成山峰 返回错误
                return False
            while left < len(arr) - 1 and arr[left] < arr[left + 1]:  # 当左指针不等于列表的最后以为，并且是递增的时候，左指针右移一格
                left += 1
            while right > 0 and arr[right - 1] > arr[right]:  # 当右指针大于0，并且递减的时候， 右指针左移一格
                right -= 1
            if left == right and right != 0 and left != len(arr) - 1:  # 如果 左右指针重合，并且不在index[0] （列表最左侧）
                # 和index[len(arr)]（列表最右侧）的时候返回正确值 否则返回错误值
                return True
            else:
                return False

