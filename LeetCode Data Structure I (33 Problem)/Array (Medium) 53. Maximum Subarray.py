class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]  # 创建一个max,value = 第一个数字
        tmp = 0  # 创建一个临时变量 =0
        for i in range(0, len(nums)):  # 遍历一次
            tmp += nums[i]  # 把每一个数字都加到临时变量tmp里面

            if (tmp > max):  # 如果临时变量>max 那把就把max修改成临时变量
                max = tmp

            if (tmp < 0):  # 如果临时变量<0,说明加的数字都是负数,为负收益 把tmp设置为0 重新开始.

                tmp = 0
        return max


"""整个循环就是,
设置 max = -2, tmp =0, 
第一次循环tmp = -4,reset 到0
第二次循环temp = 1, 1>0 所以max = 1
第三次循环temp = -2, reset到0 ，max数值不变
第四次循环temp = 4, max=4
第五次循环 temp = 3, max = 4
第六次循环 temp =5, max =5
第七次循环 temp = 6, max = 6
第八次循环 temp = 1, max = 6
第九次循环 temp =5, max =5 
循环结束 返回最大值 6"""   