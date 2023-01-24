# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.s = set()  # 创建一个哈希表

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        if k - root.val in self.s:  # 如果k-root.val在哈希表中 返回值
            return True
        self.s.add(root.val)  # 不然就把root.val加入到哈希表中
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)  # 向左递归， 和向右递归
