class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: # 如果不是矩阵，或者空矩阵 返回空列表
            return list()
        row = len(matrix)        # 行等于矩阵的长度
        column = len(matrix[0])        # 列 等于矩阵[0]的长度
        left, right, top, bottom = 0, column - 1, 0 , row - 1
        # 定义一个左，右，上，下
        # 其中 左为0, 右等于column-1 因为0 index, 上等于0, 下等于rows -1
        # 左右等于x, 也就是range(0,column - 1)
        # 上下等于y, 也就是range(0, rows - 1)
        final_list = []
        # 创建一个最终返回列表用于添加元素
        while left <= right and top <= bottom:                  # 外循环 当左右没跑完 并且上下没跑完的情况下
            for column in range(left, right + 1):               # 从左往右遍历，并且把访问过的元素依次添加到最终列表里
                final_list.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):              # 从上往下遍历,因为最右上角的元素访问过了,所以这次从top+1开始访问
                final_list.append(matrix[row][right])
            if left < right and top < bottom:                   # 这里做一个判定，确保 左右不相等，并且 上下不相等，如果相等了 那么就说明我们
                                                                # 要么只剩下一行 或者 只剩下一列，那么下面的循环就不需要跑，只需要再跑一次上面2个循环
                                                                # 其中的一个即可
                for column in range(right - 1, left, -1):       # 从右往左遍历,index依次递减
                    final_list.append(matrix[bottom][column])   # 填充访问元素
                for row in range(bottom, top, -1):              # 从下往上遍历, index依次递减
                    final_list.append(matrix[row][left])        # 填充访问元素
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
            # 当跑完了一整个大循环之后, 左和上分别加1, 右和下分别减1.
        return final_list
        # 时间复杂度 O(mn),m和n 分别为矩阵的行数和列数。矩阵中的每个元素都要被访问一次。
        # 空间复杂度 O(1),除了输出数组以外, 空间复杂度是常数
