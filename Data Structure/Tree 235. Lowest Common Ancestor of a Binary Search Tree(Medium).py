# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 迭代法 iteration
        while root:  # 当root不为空的时候持续遍历
            if root.val > p.val and root.val > q.val:  # 如果当前node比 p和q都大，往左遍历
                root = root.left
            elif root.val < p.val and root.val < q.val:  # 如果当前Node 比p和q都小， 往右遍历
                root = root.right
            else:  # 如果node在2个中间 直接返回当前的node
                return root
