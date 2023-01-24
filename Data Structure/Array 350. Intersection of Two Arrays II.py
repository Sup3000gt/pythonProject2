class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #排序解法 或者 数组已经排序了
        nums1.sort()
        nums2.sort()

        my_list = []
        index1 = index2 = 0
        while index1 < len(nums1) and index2 < len(nums2): #当指针1<列表1长度 and 指针2<列表2长度时
            if nums1[index1] < nums2[index2]:#如果列表[index1]<列表2[index2] 那么 指针1 + 1
                index1 += 1
            elif nums1[index1] > nums2[index2]:#如果列表[index1] > 列表2[index2] 那么 指针2 + 1
                index2 += 1
            else:
                my_list.append(nums1[index1]) #如果等于 那么把等于的这个数字加入列表, 指针1指针2 都加1
                index1 += 1
                index2 += 1

        return my_list #返回列表
    # 时间复杂度： O(mlogm+nlogn),