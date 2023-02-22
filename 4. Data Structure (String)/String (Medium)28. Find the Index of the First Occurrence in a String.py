"""
                            经典KMP算法
    KMP算法 核心为 next数组,next数组 就是一个前缀表(prefix table)
前缀表 主要是利用模式串中重复的字符, 把重复的字符记录下来，当主串和模式串不匹配的时候
不需要从头再来，而是直接退回到之前已经匹配过的部分。模式串中重复的部分越多,KMP算法就越省时
KMP算法的时间复杂度是O(m+n),m是主串 n是模式串的长度。

    前缀表的核心理念就是找出 前缀 与 后缀 最长的相等字符串，拿模式串 “aabaaf” 来举例
"aabaaf" 的前缀表是 "010120"
如果用作next数组 可以用2种实现方式,一种是 把前缀表右移 变成 "-1,01012"
另一种是 把前缀表整体减一 "-1,0,-1,0,1,-1"
之所以要把前缀表右移或者减一作为next数组 是以为 当文本串和模式串发生冲突的时候,我们可以
直接查看 冲突位置所对应的next数组index而不是看前一位
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(needle)                             # 获取 主字符串 和 模式串的长度
        b = len(haystack)
        if a == 0: return 0                         # 如果主字符串什么也没有 那么返回0
        i = j = 0                                   # 创建2个指针j和j 分别指向 主串和模式串的index[0]
        next = self.getNext(a, needle)              # 呼叫我们写的next函数 获取next数组 然后命名为 next
        while i < b and j< a:                       # 当 i 不大于主串长度, j 不大于 模式串长度 说明没有跑完
            if j == -1 or needle[j] == haystack[i]:
                i += 1                              # 如果 i 和 j 指向的字符都一样 那么 i 和 j 都右移 继续检查下一个字符
                j += 1
            else:                                   # 如果不匹配 那么就把 j 移动到 next[j] 所对应的index上， 然后继续匹配
                j = next[j]
        if j == a:                                  # 如果 j 可以顺利的走完 那么就说明 在 主串中是包含着完整的模式串的
            return i - j                            # 那么用主串的指针 i 减去 j的 值 就可以得到对应的下标
        else:                                       # 哪怕这个时候 i 没有走完也没有关系，因为我们不需要再往下走了
            return -1                               # 如果 j 不能顺利的走完 说明 主串 不包含 模式串 返回 -1

    def getNext(self, a, needle):                   # 写一个函数用于获取next数组,参数是"模式串的长度" 和 "模式串"
        next = ['' for i in range(a)]               # 创建一个空的列表，因为 next数组返回的是模式串的最长公共前后缀 所以长度一定
                                                    # 不会超过模式串的长度，所以这个空列表的长度为 模式串的长度即可
        j, k = 0, -1                                # 创建2个指针 j, k  j指针不会后退 k指针会因为字符串是否匹配而后退
        next[0] = k                                 # k 从-1 开始, 然后因为我们前缀表右移了,所以我们next[0]永远是-1 也就是k
        while j < a-1:                              # j指针开始循环,一直循环到整个模式串的结尾
            if k == -1 or needle[k] == needle[j]:   # 因为我们调用的needle[k] 而 index最低是0,所以不存在needle[-1],那么我们前面就要
                                                    # 加一个判定如果 k == -1 说明我们的k已经在起点了 那么可以开始循环
                k += 1                              # k 和 j 都右移一位, 然后我们要记录下j的值,j的值就是k所对应的index
                j += 1
                next[j] = k
            else:                                   # 如果 k 和 j 指向的字符不等,那么k指针就往左移动, 接下来再次判定if循环
                k = next[k]                         # 如果 needle[k]还是和[j]不等 那么 k继续左移 直到 相等或者 k 返回到 -1
        return next                                 # 最后当j遍历完成之后,所对应的next数组也就得到了

"""
当然 我们现实中可以直接用自带的index函数来写
        try:
            return haystack.index(needle)
        except:
            return -1

或者 haystack.find(needle)
当然这样写 这道题也就失去了意义了
也可以 遍历一次主串， 然后 从 i 到 i+模式串的长度 来查看是否等于 模式串
如果等于返回 i ，当然这种解法 会比较慢      
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1            
"""
