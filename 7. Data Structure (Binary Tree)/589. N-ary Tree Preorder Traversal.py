"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # 递归
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(node):                      # 递归函数
            if not node: return             # 如果node等于空 返回,base case
            ans.append(node.val)            # 否则把node的值加入到 answer列表中
            for child in node.children:     # 然后对全部的孩子进行递归
                dfs(child)                  # 递归函数
        dfs(root)                           # 呼叫函数
        return ans                          # 返回最终列表
