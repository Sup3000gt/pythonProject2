class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:  # 如果字符串不是偶数那么肯定无法匹配直接返回错误值
            return False
        dic = {'}': '{', ']': '[', ')': '('}  # 创建一个哈希表，构建左右括号对应关系
        stack = []
        for c in s:  # 遍历整个字符串
            if c in dic:  # 如果c在字典里，那么说明是右括号 进行判定
                if not stack or stack[-1] != dic[c]:  # 如果stack是空的或者 栈顶和右括号不匹配 那么返回False
                    return False
                stack.pop()  # 如果匹配 那么把栈顶的元素去除
            else:  # 如果不在字典里 说明是左括号，进行入栈操作
                stack.append(c)
        return not stack  # 如果 stack为空 那么会返回False, 所以我们最后返回的时候要 返回 not stack,而不是 stack
