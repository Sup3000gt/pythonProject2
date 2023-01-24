class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #解法1
        if len(ransomNote) > len(magazine): #如果ransomeNote比magazine长 ，那直接返回False
            return False
        else:
            for char in ransomNote: #遍历整个ransomNote， 如果不在magazine里直接返回no,
                if char not in magazine:
                    return False
                else: #如果在 那就把那个字符串替换为"", string.replace(oldvalue, newvalue, count)
                    magazine = magazine.replace(char,"",1)
        return True


"""     解法2：
        if len(magazine) < len(ransomNote):
            return False
        counter = {}  # 创建空的哈希表
        for i in magazine:  # 先遍历magazine， 如果i 不在哈希表里，添加到哈希表中
            if i not in counter:
                counter[i] = 0
            counter[i] += 1
        for j in ransomNote: #然后遍历ransomNote，如果 不在哈希表中，直接返回False
            if j not in counter:
                return False
            elif j in counter and counter[j] >= 1: #如果在哈希表中，并且counter[j]的值 >= 1,那么减1
                counter[j] -= 1
            else: #如果在哈希表中，但是counter[j]的数值已经比1小了，也就是说是0了，那么我们也没有足够的数量完成construction
                return False #例如 magazine = "aa", 但是ransomNote = "aaa" 此时我们需要3个a，但是我们只有2个a
        return True #如果以上全错误判定全没生效 那么返回True
"""
"""        解法3:
        m = list(magazine) 把2个字符串都变成list
        r = list(ransomNote)
        for i in range(0, len(m)): 遍历整个m,如果这个字符在r里面,那么就把这个字符从m这个列表里移除.
            if m[i] in r:
                r.remove(m[i])
        if len(r) == 0: 如果最后r列表空了,代表里面所有字符可以由 m 里的字符构成，返回True
            return True
        else: 不然说明 不足以达成构筑 返回 False
            return False
"""













