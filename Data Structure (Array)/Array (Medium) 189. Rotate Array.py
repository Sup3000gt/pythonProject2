class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针， 先写一个function reverse, reverse有2个参数i,j
        def reverse(i,j):
            while i < j:  # i是左指针,j是右指针，当左指针小于右指针的时候
                nums[i],nums[j] = nums[j],nums[i] # 交换左右指针的数值
                i += 1  # 左指针右移一格
                j -= 1  # 右指针左移一格
                        # 当左右指针重叠的时候 或者 左指针在右指针 右边的时候 循环结束
                        # 说明我们已经把整个左右指针范围内的元素全部反转了
        n = len(nums)   # 设一个变量 n 等于 数组的长度
        k %= n          # 然后 k= k%n ,为什么要用% 是因为要排除k比n大的情况，
                        # 如果数字只有10个元素,k等于15，那么等于从第五个元素开始反转
        reverse(0, n - 1)   # 首先第一次反转 之后得到 [7,6,5,4,3,2,1]，参数是整个列表
        reverse(0, k - 1)   # 第二次反转 得到 [5,6,7,4,3,2,1] 参数是从0到k的左边，因为例题k = 3,那么我们反转0,1,2三个元素 得到5,6,7
        reverse(k, n - 1)   # 第三次反转 得到 [5,6,7,1,2,3,4] 参数是从k到列表的长度,也就是反转 列表的后半部分
