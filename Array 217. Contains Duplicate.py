class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = {} #创建空的哈希表
        for i in nums: #第一次遍历 如果i 不在哈希表里，那么哈希表[i]=0,
            if i not in counter:
                counter[i] = 1
            else: #如果已经存在哈希表里 那么说明这个数字是第二次出现了，返回 True
                return True