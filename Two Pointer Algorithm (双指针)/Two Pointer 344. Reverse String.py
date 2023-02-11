class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 双指针
        left = 0
        right = len(s) - 1
        while left < right:     #   当左右 指针没遇到 则一直循环
            s[left], s[right] = s[right], s[left]   # 交换左右指针的value
            left += 1                               # 左右指针各往中间前进一位
            right -= 1