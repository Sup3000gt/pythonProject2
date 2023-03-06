"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections


# 这一题就是层序遍历的变种
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue = collections.deque()
        if root:
            queue.append(root)
        depth = 0 #记录深度 使用层序遍历
        while queue:
            size = len(queue)
            depth += 1
            for i in range(size): #外循环是队列的长度
                node = queue.popleft()
                for j in range(len(node.children)): #内循环是孩子的长度
                    if node.children[j]:
                        queue.append(node.children[j])
        return depth #最后返回 深度