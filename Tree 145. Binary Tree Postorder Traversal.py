# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 前序翻转
        # 交换一下原本前序遍历中，left和right的位置,即可得到[根|右|左] 的遍历结果
        # 然后对遍历结果进行反转 就可以得到 [左|右|根]
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            res.append(cur.val)
        return res[::-1]

# 后序遍历-递归-LC145_二叉树的后序遍历
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def traversal(root: TreeNode):
            if root == None:
                return
            traversal(root.left)    # 左序
            traversal(root.right)   # 右序
            result.append(root.val) # 打印

        traversal(root)
        return result

