"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(node):                                  # 递归函数
            if not node: return                         # 如果node等于空 返回,base case
            for child in node.children:                 # 然后对全部的孩子进行递归
                dfs(child)                              # 递归函数
            res.append(node.val)                        # 否则把node的值加入到 result列表中
        dfs(root)                                       # 呼叫函数
