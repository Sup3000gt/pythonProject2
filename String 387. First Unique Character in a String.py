def firstUniqChar(s):
    counter = {}  # 创建空的哈希表
    for i in s:  # 第一次遍历 如果i 不在哈希表里，那么哈希表[i]=0,
        if i not in counter:
            counter[i] = 0
        counter[i] += 1
    for j in counter:  # 遍历一次哈希表，如果遇到value 为1的值则返回那个值的index
        if counter[j] == 1:
            return s.index(j)
    return -1  # 如果遍历完都没找到1 说明全都重复了 返回-1


s = "loveleetcode"


print(firstUniqChar(s))
