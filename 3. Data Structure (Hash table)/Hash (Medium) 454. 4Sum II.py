class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = {}                        # 首先创建一个空的哈希表 用来存储 nums1 和nums2 的和
        for n1 in nums1:                    # 双循环 把列表1和列表2 的每一个数字的和加在一起
            for n2 in nums2:
                if n1+n2 in hashmap:        # 如果这个和出现在 哈希表中， 那么就把对应的value+1
                    hashmap[n1+n2] += 1
                else:
                    hashmap[n1+n2] = 1      # 如果没有，那么就把这个对应的值 设置为 1
        count = 0                           # 设置一个计数器
        for n3 in nums3:
            for n4 in nums4:                # 双循环 列表3和列表4
                key = -n3 - n4              # key = 0 减去 列表3和列表4中 2个元素的和
                if key in hashmap:          # 如果 key 在 哈希表中找到了， 说明 列表1和2中 元素的和 刚好有可以和 列表3和列表4元素的
                    count += hashmap[key]   # 和 互补， 那么key所对应的value就要加到count上面
        return count                        # 最后返回我们的计数器， 这样的遍历方式可以只用O的2次方时间复杂度来解决问题
