# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 解法1 递归 前序遍历
        if not root:
            return None
        root.left, root.right = root.right, root.left  # 中，交换node里面的左和右
        self.invertTree(root.left)      # 左
        self.invertTree(root.right)     # 右
        return root  # 返回根节点
        # 在这里 如果把Line12 和放到line15那就是 后序遍历

        # 解法2 迭代 深度优先遍历（前序遍历）
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = [root] # 创建一个stack,把root 加入到栈中
        while stack:
            node = stack.pop() # 每次循环弹出栈顶的元素，
            node.left, node.right = node.right, node.left  # 中，交换它的左右子树，如果左右子树存在就加入栈中
            if node.right:
                stack.append(node.right)  # 右
            if node.left:
                stack.append(node.left)  # 左
        return root #26/27和28/29行的代码可以互换
