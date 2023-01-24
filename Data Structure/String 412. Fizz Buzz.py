class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [] #创建一个空列表
        for i in range (1, n+1): #遍历从1开始到n+1的数字
            if i % 5 == 0 and i % 3 == 0: #能被15整除
                answer.append("FizzBuzz")
            elif i % 5 == 0: #能被5整除
                answer.append("Buzz")
            elif i % 3 == 0: #能被3整除
                answer.append("Fizz")
            else: #不然返回str(i)
                answer.append(str(i))
        return(answer)