class Solution:
    # 1. 翻转字符数组
    def reverse_string(self, text, left, right):  # 这里用双指针法 写一个函数 用来反转一段字符串， 也就是344题的答案
        while left < right:  # 但是这里不需要定义左右指针,因为左右指针的参数已经给了
            text[left], text[right] = text[right], text[left]
            left += 1
            right -= 1
        return text

    # 2. 去除多余的空格
    def remove_space(self, s):  # 写一个函数用来去除 空格
        n = len(s)
        left, right = 0, n - 1  # 双指针

        while left <= right and s[left] == ' ':  # 检查字符串第一位 是不是空格， 如果是 那么就把左指针右移一位
            left += 1  # 去除开头多余的 空格
        while left <= right and s[right] == ' ':  # 检查 字符串最后一位是不是空格， 如果是 就把右指针左移。
            right -= 1  # 去除结尾多余的 空格

        tmp = []  # 创建一个空的列表
        while left <= right:  # 当左右指针还没相交的情况下 去掉中间2个单词中间多余的空格
            if s[left] != ' ':  # 如果当前字符串 不是空格 添加到 列表中
                tmp.append(s[left])
            elif tmp[-1] != ' ':  # 当前位置是空格，但是相邻的上一个位置不是空格，那么这个空格是合理的 添加进列表
                tmp.append(s[left])
            left += 1  # 最后 左指针 持续右移
        return tmp  # 最后返回 全部多余空格都去除过的 列表

    # 3. 反转每个单词
    def reverse_each_word(self, word):
        start, end = 0, 0  # 创建2个指针 用于记录 每一个单词的第一个字母和结尾
        n = len(word)
        while start < n:  # 遍历整个 字符串
            while end < n and word[end] != " ":  # 如果当前字符不是 空格 那么 end指针就右移 直到遇到空格
                end += 1
            self.reverse_string(word, start, end - 1)  # 当遇到空格的时候， 我们用写的第一个函数来把这个单词反转，函数的
            # 参数是， 当前字符串，起始位置为start 指针 第一个单词的话 应该为0，结尾指针
            # 则是 end-1 因为 end指向的是空格,所以我们反转 从0到end-1的这一整个单词
            start = end + 1  # 反转完毕之后把start指针 指向end下一个字母 也就是第二个单词的第一个字母
            end += 1  # 然后 end指针右移 也移动到第二个单词的第一个字母， 开始第二次循环
            # 直至整个字符串遍历完毕
        return None

    def reverseWords(self, s: str) -> str:
        # 最后用写好的函数 来返回 最终结果                      测试用例："the sky is blue"
        l = self.remove_space(s)  # 首先用remove_space去除全部多余的空格 然后定义一个变量 l.
        # 输出：['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']

        self.reverse_string(l, 0, len(l) - 1)  # 之后用 reverse_string 把整个字符串都反转
        # 输出：['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']

        self.reverse_each_word(l)  # 然后用 reverse_each_word 再把每个单词反转过来
        # 输出：['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']

        return "".join(l)  # 最后因为l是列表， 再用.join把列表合并成字符串
        # 输出：blue is sky the


"""    用python自带的split 解法 但是算是作弊
class Solution:
        def reverseWords(self, s: str) -> str:
            s = s.split()
            str = " ".join(s[::-1])
            return str
"""
