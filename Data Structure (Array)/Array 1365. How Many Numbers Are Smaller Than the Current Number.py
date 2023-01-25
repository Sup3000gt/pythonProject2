class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 解法1： 暴力破解 O(n^2)
        lst = []
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            lst.append(count)
        return lst
    # 解法2：排序
        result = sorted(nums)
        hash = {}
        for i,num in enumerate(result):
            if num not in hash.keys():
                hash[num] = i
        for i,num in enumerate(nums):
            result[i] = hash[num]
        return result
