class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        evenIndex = 0 # 偶数指针
        oddIndex = 1 # 奇数指针
        for i in range(len(nums)):
            if nums[i] % 2: # 如果是奇数从1开始加入到列表，每加入一次奇数指针+2
                result[oddIndex] = nums[i]
                oddIndex += 2
            else: #否则就是偶数，从0开始加入到列表，然后每加入一次偶数指针+2
                result[evenIndex] = nums[i]
                evenIndex += 2
        return result
