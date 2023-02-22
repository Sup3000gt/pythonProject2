class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 标准 二分查找
        # 如果 x*x = num ,那么 一定满足 1 <= x <= num
        left,right = 1,num
        while left <= right:
            mid = (left+right)//2
            square = mid*mid
            if square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
            else:
                return True
        return False
        # 时间复杂度 O(logn)
        # 空间复杂度 O(1)
