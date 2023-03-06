class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 解法1：先用大饼干喂饱大胃口
        g.sort() # 首先要排序
        s.sort()
        count = 0 # 变量记录喂饱的人数
        lengthOfS = len(s)-1 #饼干的index
        for i in range (len(g)-1,-1,-1): # 遍历胃口，从大大小
            if lengthOfS >= 0 and s[lengthOfS] >= g[i]: # 然后选择最大的饼干,如果这个饼干可以满足这个胃口
                count += 1                              # 那么 喂饱人数加一, 饼干index减一
                lengthOfS -= 1
        return count

        # 解法2： 优先喂饱小胃口
        # g.sort()
        # s.sort()
        # res = 0                                         # 记录喂饱的人数
        # for i in range(len(s)):                         # 遍历饼干
        #     if res <len(g) and s[i] >= g[res]:          # 首先判定 喂饱的人不能超过总人数，如果这个饼干可以满足
        #         res += 1                                # 那么满足人数加一,并且用人数作为index,下次就开始喂第二个人
        # return res                                      # 而不是第一个
