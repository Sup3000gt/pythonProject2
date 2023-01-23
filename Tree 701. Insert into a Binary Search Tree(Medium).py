# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 解法1： 递归

        # 返回更新后的以当前root为根节点的新树，方便用于更新上一层的父子节点关系链

        # Base Case
        if root == None:  # 如果遇到空节点 说明循环到叶子节点了，那么就把这个新节点设为叶子节点
            return TreeNode(val)

        # 单层递归逻辑:
        if val < root.val:
            # 将val插入至当前root的左子树中合适的位置
            # 并更新当前root的左子树为包含目标val的新左子树
            root.left = self.insertIntoBST(root.left, val)
        if val > root.val:
            # 将val插入至当前root的右子树中合适的位置
            # 并更新当前root的右子树为包含目标val的新右子树
            root.right = self.insertIntoBST(root.right, val)

        # 返回更新后的以当前root为根节点的新树
        return root
