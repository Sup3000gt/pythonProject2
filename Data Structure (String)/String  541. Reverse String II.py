class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse_substring(text):  # 这里用双指针法 写一个函数 用来反转一段字符串， 也就是344题的答案
            left, right = 0, len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text

        res = list(s)  # 把字符串变成列表

        for cur in range(0, len(s), 2 * k):  # 然后遍历整个列表, 每次递进2k
            res[cur: cur + k] = reverse_substring(res[cur: cur + k])
            # 在这里 我们把从cur 到 cur+k的字符串 放到reverse函数里面 然后再替换掉原本的list
        return ''.join(res)  # 最后用Join把列表再合并成字符串
