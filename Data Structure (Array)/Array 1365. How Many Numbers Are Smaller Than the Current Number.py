# 解法2：排序
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = sorted(nums)  # 先排序
        hash = {}  # 创建一个空的哈希表
        for i, num in enumerate(result):  # 从小到大排序之后，元素下标就是小于当前数字的数字 i是index,num 是列表里index对应的数值
            # print(result)            如果打印 result 那么此刻的列表是 [1, 2, 2, 3, 8]
            if num not in hash.keys():  # 遇到了相同的数字，那么不需要更新该 number 的情况
                hash[num] = i  # 第一个for loop 跑完 我们的哈希表会是这样的{1: 0, 2: 1, 3: 3, 8: 4}
        for i, num in enumerate(nums):  # 然后再根据这个哈希表给对应的result赋值
            result[i] = hash[num]  # 我们的result的起始值为 [1, 2, 2, 3, 8],num顺序为[8, 1, 2, 2, 3]
            # 接下来在哈希表中找对应的num的value,第一个是8对应的是4，所以替换4，第二个是1所以替换0以此类推
            # [4, 2, 2, 3, 8]
            # [4, 0, 2, 3, 8]
            # [4, 0, 1, 3, 8]
            # [4, 0, 1, 1, 8]
            # [4, 0, 1, 1, 3]
        return result  # 最后返还 result列表
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


