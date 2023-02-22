from collections import deque


class MonotonicQueue:  # 创建一个单调队列的类
    def __init__(self):  # 用双端队列来实现
        self.queue = deque()
        # 双端队列需要的几个方法, push, pop , front

    def pop(self, value):  # 用来弹出元素
        if self.queue and value == self.queue[0]:  # 确认队列是否为空,比较弹出的数值是否等于队列出口元素的数值
            self.queue.popleft()  # 如果相等则弹出队列最左边的元素也就是最大值,如果不是 则不弹出

    def push(self, value):  # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出
        while self.queue and value > self.queue[-1]:  # 直到push的数值小于等于队列入口元素的数值为止
            self.queue.pop()
        self.queue.append(value)  # #这样就保持了队列里的数值是单调从大到小的了

    def front(self):  # 查询队列最前端的元素 也就是0 index的元素,因为 单调队列是从大到小的
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MonotonicQueue()  # 创建一个队列 和 最终返回的列表
        res = []
        for i in range(k):  # K是滑动窗口的长度，把k前的元素加入到单调队列里面
            que.push(nums[i])
        res.append(que.front())  # result 列表中把最大的元素加入进去
        for i in range(k, len(nums)):  # 因为上面的滑动窗口循环 已经把k之前的元素都加入了,第二个loop就从k开始循环到nums列表的尾部
            que.pop(nums[i - k])  # 滑动窗口去掉队列中最前面的元素
            que.push(nums[i])  # 滑动窗口 在尾部添加下一个新的元素
            res.append(que.front())  # 把目前队列中的最大值记录下来 保存到result里面
        return res  # 返回 res 列表

# 简易版写法
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()    # 创建一个 双向队列
        for n in nums[:k]:  # 循环滑动窗口长度
            while dq and n > dq[-1]:    # 如果队列不为空，并且n 大于队列最尾部的元素
                dq.pop()                # 就把队列最尾部的元素pop出去 直到 队列里没有比n大的元素
            dq.append(n)                # 这时把n 添加到队列中
        res = [dq[0]]                   # 创建一个 res列表 用于记录， 记录的对象永远是 队列中的第一个元素 dq[0]
        l = 0                           # 创建一个 l = 0 的指针
        for r in range(k, len(nums)):   # 然后开始从k 遍历到nums的尾部
            if nums[l] == dq[0]:        # 如果 nums[l] 等于队列的头部元素 或 最大元素 就把 头部元素弹出去
                dq.popleft()            # nums[l]是滑动窗口的左侧 l=0也就是 nums[0]也就是滑动窗口最左侧
            l += 1                      # 否则 l 指针右移
            n = nums[r]                 # n 指向 滑动窗口的右侧 如果k=3 那么 n起始点是滑动窗口右侧的第一个元素
            while dq and n > dq[-1]:    # 如果队列不为空 并且 滑动窗口右侧的元素 大于 队列的尾部元素 就把队列尾部元素弹出
                dq.pop()
            dq.append(n)                # 直到 队列中没有比n小的元素了，那么把n加入到队列
            res.append(dq[0])           # 然后 用res记录 当前队列最大值，然后r+1开始下一次循环直至结束
        return res                      # 最后返还 res
