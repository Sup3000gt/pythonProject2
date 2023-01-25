class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        result = {} # 创建一个哈希表
        for i in arr: # 全部数字里面的元素 和出现的次数添加到哈希表中
            if i not in result:
                result[i] = 0
            result[i] += 1

        checkMap={} # 创建一个新的检查哈希表
        for val in result.values(): # 循环第一个哈希表的全部value值,如果 出现在checkMap里面 说明有重复，否则就添加进 checkMap里面
            if val in checkMap:
                return False
            else:
                checkMap[val]=1
        return True