class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted = [] #创建一个空的列表
        pointer1, pointer2 = 0, 0 #创建2个指针分别对应2个需要循环的列表
        while pointer1 < m or pointer2 < n: #当指针小于m 或者 n 说明 列表还没有空
            if pointer1 == m: #如果指针1==m,说明列表1已经空了，那么依序把列表2剩余的数字按照指针2加入到sorted列表中
                sorted.append(nums2[pointer2])
                pointer2 += 1
            elif pointer2 == n:#如果指针2==n,说明列表2已经空了，那么依序把列表1剩余的数字按照指针1加入到sorted列表中
                sorted.append(nums1[pointer1])
                pointer1 += 1
            elif nums1[pointer1] < nums2[pointer2]: #如果两个都没空,那么如果指针1的数字比指针2的数字小,那么吧指针1的数字添加到sorted列表中
                                                    #指针1往右移动一格
                sorted.append(nums1[pointer1])
                pointer1 += 1
            else:                                   #反之，指针2的数字更小加入到列表，然后指针2 往右移动一格
                sorted.append(nums2[pointer2])
                pointer2 += 1
        nums1[:] = sorted                         #[:]makes a shallow copy of the array
