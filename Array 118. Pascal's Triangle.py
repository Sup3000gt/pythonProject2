class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [] #创建一个空的大list
        for i in range(numRows): #第一个循环,每一个循环都创建一行
            row = []
            for j in range(0, i + 1): #第二个循环， 因为有numRows行,所以循环要 numRows+1
                if j == 0 or j == i: #i是每一行的最后一个数字,j是每一行的第一个数字，都是1，所以直接append(1)
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1]) #第i行的第j个数字 等于第[i-1]行[j-1]个的数字+第[i-1]行第[j]个之和
            ret.append(row) #把row 加入到大的列表中去
        return ret #返回大列表