from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()
    def push(self, x: int) -> None:
        # 直接append 在deque里面即可
        self.queue.append(x)
    def pop(self) -> int:
        # 首先确认 deque不是空的
        if self.empty():
            return None

        # 因为队列 FIFO 的特性,所以我们需要遍历整个队列，除了最后一个元素。然后把整个队列重新加入到队列里面
        # 假设 deque = [1,1,1,2] 遍历过后 deque =[2,1,1,1]
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
        # 这个时候 我们return popleft(), 因为 2是队列的第一个元素 所以会被第一个弹出去
        return self.queue.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        # 因为python [-1] 会返回最后一个元素,所以如果要查询栈顶 只需要用quequ[-1]即可
        return self.queue[-1]
    def empty(self) -> bool:

        # 这里我们可以直接 return not self.queue
        return len(self.queue) ==0

