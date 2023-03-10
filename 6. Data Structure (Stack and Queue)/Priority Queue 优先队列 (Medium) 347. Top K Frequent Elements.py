import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}  # 创建一个dictionary, 统计元素出现频率
        for i in nums:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1

        # 创建一个 优先队列 也就是 heap
        pri_que = []  # 创建一个空的小顶堆
        for number, frequency in myDict.items():  # 扫描所有频率的数值,然后按从小到大的顺序加入到 小顶堆中
            heapq.heappush(pri_que, (frequency, number))
            if len(pri_que) > k:  # 因为我们只需要维护K个元素在优先队列里面,所以如果优先队列的长度大于K 我们就把堆顶弹出
                heapq.heappop(pri_que)

        res = [0] * k  # 创建一个k长度的空列表
        for i in range(k - 1, -1, -1):  # 从k-1开始遍历到0 ,每次 i -1
            res[i] = heapq.heappop(pri_que)[1]  # 开始弹出堆顶的元素，因为小顶堆的特性，所以我们要用倒序来输出到数组,
        return res  # res[i] = res[k-1],res[k-2],res[k-3] 以此类推，最后返回数组


""" 
range()函数用于生成一个整数序列：
range(start, stop, step)：生成一个从start开始，到stop-1结束的整数序列，步长为step。
在这个例子中，range(k-1, -1, -1)的意思是生成一个从k-1开始，到-1结束的整数序列，步长为-1。这个序列用于在循环中逆序遍历列表。

优先队列常常使用堆（Heap）数据结构来实现。堆是一种二叉树，可以用数组或列表来表示，它具有以下特性:
        堆中每个节点的值都必须大于或等于（或小于或等于）其子节点的值。
        堆总是一棵完全二叉树，除了最后一层外，每一层都是满的，并且最后一层的节点都靠左排列。
        
优先队列是一种可以让元素按优先级（或权值）排序的队列。在优先队列中，每个元素都有一个优先级，
优先级越高的元素排在队列的前面。当新的元素加入队列时，它会插入到合适的位置，以保证队列中的元素始终按照优先级有序。
堆可以用于实现优先队列，常见的实现方式有两种：

最小堆：堆中的每个节点的值都小于或等于其子节点的值，因此堆顶元素是堆中的最小值。
最大堆：堆中的每个节点的值都大于或等于其子节点的值，因此堆顶元素是堆中的最大值。
在Python中，可以使用heapq模块来实现优先队列。heapq提供了一些函数，可以对一个列表进行堆操作，
包括将一个列表转换为堆、从堆中弹出最小或最大值、将一个元素插入到堆中等等。这些函数实现了最小堆（即小顶堆）的功能，
但通过使用取反等操作，可以实现最大堆（即大顶堆）的功能。

"""
# 时间复杂度：O(nlogk)
# 空间复杂度：O(n)

