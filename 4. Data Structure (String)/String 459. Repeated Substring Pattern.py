class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 解法1 移动窗口
        newS = s + s        # 如果给出的字符串s的substring里面是有重复的 那么 2个s相加之后中间也一定会有 s
        final = newS[1:-1]  # 举例 s = abcabc 那么 s+s = abcabc+abcabc,为了避免检测到s自己 我们把开头的a和结尾的c去掉
        if s in final:      #　s+s =  bcabc+abcab ,从新的s+s中我们可以看到 中间也是包含 abcabc的 这就说明s的substring 是有循环的
            return True     # 那么返回 True
        else:
            return False    # 否则返回 False

# 当然 这题也可以用KMP方法来解 就像28题一样
