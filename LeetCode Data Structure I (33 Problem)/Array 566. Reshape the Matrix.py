class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # 解法1 往一个小列表里添加元素， 列表满了就加入到“大”列表中
        if len(mat) * len(mat[0]) != r * c:  # #如果 mat的行*列 不等于 r*c 那么说明矩阵转换不行，返回原本的矩阵
            return mat
        res, stack = [], []  # 创建一个新二维矩阵, res 是row, stack 是columns
        for row in mat:  # 外循环 循环mat的row
            for e in row:  # 内循环 循环mat row里的每一个元素 “e”
                stack.append(e)  # 把“e”加入到新创建的stack里面
                if len(stack) == c:  # 如果stack的长度 等于我们想要的columns “c” 那么说明 这个stack装满了
                    res.append(stack)  # 那么就把装满了的stack 加入到res里面
                    stack = []  # 创建一个新的 “空的”’ stack 然后返回循环继续添加下一个stack
        return res  # 最后返回2维的list of list 也就是新矩阵

    """
       解法2
        m, n = len(mat), len(mat[0]) #创建两个变量m,n 等于矩阵的行和列
        if m * n != r * c:  #如果m*n 不等于 r*c 说明不符合规则 直接返回原矩阵
            return mat

        ans = [[0] * c for _ in range(r)] #创建一个r*c的空矩阵
        # 如何创建一个空的矩阵 arr = [[0 for i in range(cols)] for j in range(rows)]
        for x in range(m * n): #循环整个mat
            ans[x // c][x % c] = mat[x // n][x % n] #然后在mat的对应的空矩阵里面赋值

        return ans #返回新矩阵"""

    """
        解法3
        还可以用numpy自带的reshape method

        M, N = len(mat), len(mat[0])
        if M * N != r * c:
            return mat
        import numpy as np
        return np.asarray(mat).reshape((r, c))"""
