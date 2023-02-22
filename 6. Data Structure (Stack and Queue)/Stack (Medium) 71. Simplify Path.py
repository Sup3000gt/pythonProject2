class Solution:
    def simplifyPath(self, path: str) -> str:
        directory = path.split("/")         # 首先用split把路径区分
        stack = []                          # 创建一个栈
        for name in directory:              # 遍历整个路径
            if name == "..":                # 如路径是 ".." 说明我们要返回上级目录
                if stack:                   # 先确定栈是否为空，如果不是就把栈顶弹出
                    stack.pop()             # 等于返回上级目录
            elif name and name != ".":      # 再判定 路径是否"." ,如果不是 那就代表是字母或数字
                stack.append(name)          # 把它们加入到栈中. 如果是"." 那么无需任何操作
        return "/" + "/".join(stack)        # 最后再把 栈中的元素 用"/" 连接成常规路径
