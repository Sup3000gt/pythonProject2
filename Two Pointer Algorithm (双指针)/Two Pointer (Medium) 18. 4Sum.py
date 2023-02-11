class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 解题思路跟 3Sum 一样 只不过多一层 for loop
        nums.sort()       # 首先 把数组排序
        n = len(nums)
        res = []
        for i in range(n-3):  # 然后还是遍历整个数组
            # a + b + c + d = target
            if i > 0 and nums[i] == nums[i - 1]:            # 对nums[i]去重,也就是去掉重复的a
                continue
            for k in range(i + 1, n-2):                     # 然后遍历k, 也就是b 因为b一定是在a后面 所以要从i+1开始遍历
                if k > i + 1 and nums[k] == nums[k - 1]:
                    continue                                # 对nums[k]去重, 去掉重复的b
                p = k + 1               # 然后 思路就跟 3Sum 一样了左右指针， 左指针 = p , 右指针 = q
                q = n - 1

                while p < q:                            # 一直循环到左右指针相交
                    if nums[i] + nums[k] + nums[p] + nums[q] > target:  # 跟 3Sum 一样 如果 大于 > target 右指针左移
                        q -= 1
                    elif nums[i] + nums[k] + nums[p] + nums[q] < target:    # 不然 左指针右移
                        p += 1
                    else:           # 如果都不是 那么就添加到最终返回的列表里
                        res.append([nums[i], nums[k], nums[p], nums[q]])
                        # 最后对nums[p]和nums[q]去重， 去掉重复的 c和d
                        while p < q and nums[p] == nums[p + 1]: p += 1
                        while p < q and nums[q] == nums[q - 1]: q -= 1
                        p += 1      # 最后 左右指针 各移一位
                        q -= 1
        return res