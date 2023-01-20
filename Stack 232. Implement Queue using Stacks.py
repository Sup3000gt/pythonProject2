class MyQueue:
    # 用双栈实现队列
    def __init__(self):  # 建立2个栈， 一个入栈，一个出栈
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:  # push操作 就直接加入到 入栈里就好
        self.stack_in.append(x)

    def pop(self) -> int:  # 出栈操作比较麻烦， 首先判定2个栈是不是都是空的
        if self.empty():  # 如果双栈都是空，返回None
            return None
        if self.stack_out:  # 接着判定 出栈out是不是空的 如果不是，那么从出栈pop
            return self.stack_out.pop()
        else:  # 如果出栈空了 empty有返回值 说明 入栈肯定不是空的，那么就把入栈里的元素全部加入到出栈。
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()  # 然后从出栈最顶上（也就是入栈最下面的那个元素） 开始pop

    def peek(self) -> int:  # 查看栈顶
        ans = self.pop()  # 先用self.pop 查看pop的值 然后保存到ans里面
        self.stack_out.append(ans)  # 之后把ans保存到出栈
        return ans  # 返回ans

    def empty(self) -> bool:  # 2个栈只要有1个不是空的 就返回False值
        return not (self.stack_in or self.stack_out)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()