class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """ 解法1：
        if len(s) != len(t): #如果长度不等，直接返回
            return False

        hashtable = {}
        for character in s: #创建一个哈希表，把其中一个字符串都丢进去
            if character not in hashtable:
                hashtable[character] = 0
            hashtable[character] += 1
        for char2 in t: #遍历第二个字符串，如果不在哈希表中 返回False,如果在哈希表中并且对应的值>1，那么value-1，不然返回false
            if char2 not in hashtable: 
                return False
            elif char2 in hashtable and hashtable[char2]>=1:
                hashtable[char2] -= 1
            elif char2 in hashtable and hashtable[char2] ==0:
                return False
        return True"""
        """
        #解法2：
        if len(s) != len(t): #如果长度不等，直接返回
            return False
        a = list(s)
        b = list(t)
        a.sort()
        b.sort()
        return a == b
"""
        #解法3：(最快的)
        if len(s) == len(t): #在2个字符串长度一样的情况下
            for i in set(s): #遍历s，然后用count 查看s里面每一个字符串出现的次数 是否等于 t里面同样字符串出现的次数
                if s.count(i) != t.count(i):
                    return False #如果不是 返回错误
            return True #如果是 返回正确
        return False #最后如果 2个字符串长度不一样 返回错误