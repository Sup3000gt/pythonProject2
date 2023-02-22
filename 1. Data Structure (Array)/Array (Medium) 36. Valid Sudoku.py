board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(board):
    # 对每一行进行判断
    for i in range(9):
        storage = [] #创建一个空list
        for j in range(9): #如果board[i][j] 不是数字 继续
            if board[i][j] == '.':
                continue
            if board[i][j] in storage: #如果board[i][j] 在list里面 返回False
                return False
            else: #不然把board[i][j]添加到空的列表里
                storage.append(board[i][j])
    # 对每一列进行判断 重复上面的判定，把j和i换个位置
    for i in range(9):
        storage = []
        for j in range(9):
            if board[j][i] == '.':
                continue
            if board[j][i] in storage:
                return False
            else:
                storage.append(board[j][i])
    # 对九宫格里面的小九宫格是否重复进行判断
    for i in range(0, 9, 3):  #i = (0,3,6) i = 0 判断左上,i = 3 判断中间, i=6 判断右上的小九宫格
        for j in range(0, 9, 3): #j = (0,3,6) j 同理只不过是竖着判定的
            storage = [] #创建空列表
            for x in range(0, 3): #然后因为小九宫格 只有3行和3列,那么在i和j 上 分别加上x和y就可以得到小九宫格里面的数字
                for y in range(0, 3):
                    if board[i + x][j + y] == '.': #如果不是数字 跳过
                        continue
                    if board[i + x][j + y] in storage: #如果数字在 列表里 返回错误
                        return False
                    else:
                        storage.append(board[i + x][j + y]) #如果数字不在列表里 则添加进列表
    return True #如果以上判定都没返回错误，说明 行，列 和小九宫格都对 返回True



print(isValidSudoku(board))

