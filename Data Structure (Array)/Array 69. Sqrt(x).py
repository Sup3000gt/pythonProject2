class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分查找  
        l, r, ans = 0, x, -1    # 左指针 0， 右指针 x， 答案ans
        while l <= r:   # 当左指针小于等于右指针
            mid = (l + r) // 2 # 先求mid
            if mid * mid <= x: # 如果mid平方小于等于 x， 用ans记录下来 然后 左指针右移到middle右边
                ans = mid
                l = mid + 1
            else:       # 不然右指针移动到middle左边
                r = mid - 1
        return ans