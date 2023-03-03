class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        else:
            P = "".join(ch.lower() for ch in s if ch.isalnum()) # 去除数字和字母以外的字符 并且把字母都变成小写
            y = P[::-1]                     # 反转字符串， 然后对比字符串
            if y == P:                      # 如果一样 则是回文 否则不是
                return True
            else:
                return False
