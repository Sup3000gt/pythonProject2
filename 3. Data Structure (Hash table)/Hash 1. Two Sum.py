class Solution:
    def twoSum(self,a_list, a_number):
        hashtable = {}                              # 创建一个空的哈希表
        for i in range(len(a_list)):                # 第一次遍历
            complement = a_number - a_list[i]       # 已知a_number和i的数值 可以得到补充数complement
            if complement in hashtable:             # 如果complement不在哈希表中,则把complement添加到哈希表中第一个i
                return [i, hashtable[complement]]   # 可以得到2,把2添加到哈希表中对应0索引,第二次数字7就可以跟
            hashtable[a_list[i]] = i                # 哈希表中的2配对,返回0和1索引
