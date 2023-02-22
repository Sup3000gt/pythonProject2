class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [] # 创建一个空栈
        for c in s:
            if stack and stack[-1] == c:    # 如果栈不是空的 并且栈顶元素和c一样 那么弹出栈顶
                stack.pop()
            else:           # 不如就把c元素入栈
                stack.append(c)
        # 
        return "".join(stack)   #最后因为栈返回的是列表形式,所以用join()将栈中的字符连接为一个字符串
