class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = []    # 创建一个空栈
        operList = ["+", "-", "*", "/"] #创建一个列表 用于储存
        for s in tokens:
            if s not in operList:       # 遍历token 如果元素 不是加减乘除 那么就把元素转换成整数 并且入栈
                myStack.append(int(s))
            else:                       # 不然就把栈中最上面的2个元素 弹出
                num1 = myStack.pop()
                num2 = myStack.pop()
                if (s == "+"):          # 之后再根据 不同的运算符号 进行运算， 然后把运算结果入栈
                    myStack.append(num2 + num1)
                if (s == "-"):
                    myStack.append(num2 - num1)
                if (s == "*"):
                    myStack.append(num2 * num1)
                if (s == "/"):
                    myStack.append(int(num2 / num1))
        return myStack.pop()            # 最后返回栈顶
