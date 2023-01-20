class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float('+inf'), 0 #创建两个变量, cost = 一个无限动态变化的数字 , profit = 0
        for price in prices: #一次遍历
            cost = min(cost, price) #拿数组里面的每一个price 去跟cost对比，把cost更新到最小的数字
                                    #第一天cost = 7,第二天cost =1,第三天 cost= 1..."""
            profit = max(profit, price - cost) #之后拿profit 去跟 每一天的price-动态变化的cost 对比 求出最大
                                             #第一天 price-cost = 7-7=0,第二天 price-cost = 1-1 =0 第三天 price-cost =5-1=4
        return profit