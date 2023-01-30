class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        startX , startY = 0 , 0 # 起始点
        count = 1               # 计数器从1开始
        loop , mid = n//2 , n//2  # 循环的次数， 当n为奇数的时候,最后剩下的一个就是中心点
        matrix = [[0] * n for _ in range(n)]   # 建立一个空的n x n 矩阵

        for offset in range(1, loop + 1):           # 外面的大循环是循环多少圈，里面的4个小循环是循环正方形的四条边
                                                    # 每循环一次，offset偏移量都 加一.
            for i in range(startY, n-offset):       # 从左往右循环，横向依次往矩阵填入数字，从count开始每次加一 （上边）
                matrix[startX][i] = count           # 矩阵[startX][i] 变的只有代表列数的i，代表行数的startX没有变
                count += 1                          # 计数器每次填充完都要加一
            for j in range(startX, n-offset):       # 从上往下循环，纵向填充数字        （右边）
                matrix[j][n-offset] = count         # 矩阵[j]里面的j从0开始依次增加，代表行数从0到n-offset为止
                count += 1
            for i in range(n-offset, startY, -1):   # 从右往左循环，横向依次 从n-offset 到 startY也就是0，开始依次递减1 （下边）
                matrix[n-offset][i] = count         # 矩阵[n-offset]的行不变，[i]的列数一直从右往左的递减
                count += 1                          # 然后我们的数字也是从右往左的填充
            for j in range(n-offset, startX, -1):   # 从下往上循环，纵向填入数字 （左边）
                matrix[j][startY] = count           # 矩阵[j]一直在以递减的方式变，[starY]代表的是column 第一个循环就是0也就是第0列
                count += 1                          # 然后 依次填充count
            startX += 1                             # 最后四条边都循环结束之后,更新我们下一轮循环的起始点和偏移量
            startY += 1                             # 起始点，从[0][0]到[1][1]到[2][2]依次 x和y都 加一
            offset += 1                             # 偏移量 也是每次加一,
        if n % 2 == 1:                              # 最后判定 如果n是奇数 那么全部循环跑完还会剩下最中心的一个点
            matrix[mid][mid] = count                # 把 矩阵[mid][mid] 也就是最中心的点 填充数值count
        return matrix                               # 最后返还完整矩阵
