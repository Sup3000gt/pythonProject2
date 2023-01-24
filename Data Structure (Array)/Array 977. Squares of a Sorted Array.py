class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        final = []
        for i in nums:      # 把每个数平方
            i = i*i
            final.append(i) # 然后排序 返回
        return sorted(final)


