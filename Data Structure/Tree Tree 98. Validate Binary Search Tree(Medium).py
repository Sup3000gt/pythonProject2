# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 解法1： 递归
        # 规律: BST的中序遍历节点数值是从小到大
        pre = None  # 建立一个指针 值为None

        def _isValidBST(root):  # 写一个function
            nonlocal pre  # nonlocal  the keyword nonlocal to declare that the variable is not local
            if not root: # 如果root是None 那么是二叉搜索树 返回True
                return True
            is_left = _isValidBST(root.left) # 中序遍历 左
            if pre and pre.val >= root.val: #中序遍历 中，判断 如果pre指针指向的前一个值大于等于当前root的值 返回错误
                return False
            pre = root # 然后把pre的指针移动 到root 进行下一次判断
            is_right = _isValidBST(root.right) # 中序遍历 右
            return is_right and is_left # 如果左右遍历同时正确 那么就会返回True 否则False

        return _isValidBST(root)
