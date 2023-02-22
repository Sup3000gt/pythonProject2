class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 暴力解法 Brute Force
        final = []
        for i in nums:  # 把每个数平方
            i = i * i
            final.append(i)  # 然后排序 返回
        return sorted(final)
        # Time comp: O(n+nlogn)

        # 解法2：双指针 # Time comp: O(n)

        # 数组其实是有序的， 只不过负数平方之后可能成为最大数了。
        #
        # 那么数组平方的最大值就在数组的两端，不是最左边就是最右边，不可能是中间。
        #
        # 此时可以考虑双指针法了，i指向起始位置，j指向终止位置。

    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j, k = 0, n - 1, n - 1
        ans = [-1] * n  # 创建一个长度跟nums一样的列表,每一位都是-1
        while i <= j: # 当左指针小于等于右指针时，比较左指针和右指针指向的值的平方
            left = nums[i] ** 2
            right = nums[j] ** 2
            if left > right:     # 把大的那个加入到新列表的k的位置,因为k=n-1 所以等于从新列表的尾巴一直添加到头部
                ans[k] = left
                i += 1
            else:
                ans[k] = right
                j -= 1
            k -= 1
        return ans
