class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []     # 如果数组小于3 那么直接返回空列表
        ans = []                # 创建一个空的返回List用于储存结果
        n = len(nums)
        nums.sort()             # 重新排列整个数组

        # 找出a + b + c = 0
        # a = nums[i], b = nums[left], c = nums[right]

        for i in range(n-2):      # 开始遍历,因为 最少需要3个数所以i也就是我们的a只需要遍历到 列表的倒数第三个数即可
            left = i+1
            right = n-1
            if nums[i] > 0:     # 因为列表排序过，所以 如果第一个元素已经大于零，那么无论如何组合都不可能凑成三元组，直接返回结果就可以了
                break
            if i >= 1 and nums[i] == nums[i-1]:     # 去掉重复的a
                continue
            while left < right:     # 当左右指针还没相交的时候
                total = nums[i] + nums[left] + nums[right]
                # total =  a      +    b    +     c
                if total > 0:    # 在这里 因为a是恒定的 # 如果total > 0 说明,b+c 有点大了，那么就把右指针 左移
                    right -= 1
                elif total < 0:  # 如果 < 0 ，说明 b+c 太小了， 那么就把左指针 右移
                    left += 1
                else:           # 如果 不大也不小 那说明 a+b+c =0 那么就把 对应的 结果加入到ans结果集中
                    ans.append([nums[i], nums[left], nums[right]])
        # 接下来 要去掉重复的b和c
                    while left != right and nums[left] == nums[left + 1]:   # 去掉重复的b
                        left += 1
                    while left != right and nums[right] == nums[right - 1]:  # 去掉重复的c
                        right -= 1
                    left += 1       # 最后把左指针右移
                    right -= 1      # 右指针左移
        return ans      # 最后返回 结果集
