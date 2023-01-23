# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 解法一: Recursion 递归
        if not root or root.val == val:  # 如果root的值为None或者 等于我们要找的值 返回root节点 递归出口
            return root
        if root.val > val:  # 如果当前节点储存的值比我们要找的值小 往左子树递归
            return self.searchBST(root.left, val)
        if root.val < val:  # 如果当前节点储存的值比我们要找的值大 往右子树递归
            return self.searchBST(root.right, val)

        # 解法二 迭代 iteration
        while root:  # 当节点不为空时
            if root.val > val:  # 如果当前节点储存的值比搜索值大，那么root = root.left 往左搜索
                root = root.left
            elif root.val < val:  # 如果当前节点储存的值比搜索值小，那么root = root.right 往右搜索
                root = root.right
            else:
                return root  # 不然就是数值一样 那么返回当前节点
        return None  # 以上3种都不是 那么说明没找到 返回None
