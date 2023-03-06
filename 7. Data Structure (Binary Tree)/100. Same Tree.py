# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:         # 如果p和q都是空的 那么是对称的
            return True
        elif not p or not q:        # 如果 p 和 q 其中一个空 一个不为空 那么不对称
            return False
        elif p.val != q.val:        # 如果p 和 q 的值 不相等 那么也是不对称的
            return False
        else:
            # 最后带入递归函数, 比较p.left 和 q.left  然后 再对比右侧
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


