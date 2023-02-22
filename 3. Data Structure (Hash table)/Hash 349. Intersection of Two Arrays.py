class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 解法1： 哈希表
        ans = {}                        # 创建一个空的哈希表
        lst = set()                     # 创建一个空的set
        for i in nums1:                 # 如果这个数字不在哈希表中 就添加进去
            if i not in ans:            # 不然 就把这个数字对应的值+1
                ans[i] = 0
            ans[i] += 1
        for j in nums2:                 # 然后遍历 数组2， 如果数字在哈希表中
            if j in ans:                # 就添加进set
                lst.add(j)
        return lst                      # 最后返回set

        # 解法2 自带的set()函数
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)     # 把数组1 和 数组2 都变成 set, set的元素都是不重复的
        s2 = set(nums2)
        return s1 & s2      # 然后返回那些 同时出现在 s1和s2里面的数字
