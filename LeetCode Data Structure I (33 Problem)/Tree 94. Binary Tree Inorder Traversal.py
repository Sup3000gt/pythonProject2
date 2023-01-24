# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 解法1：递归
# 中序遍历：左 - 打印 - 右
# 终止条件：当前节点为空时
# 函数内：递归的调用左节点，打印当前节点，再递归调用右节点
class Solution:
    def inorderTraversal(self, root):
        res = []  #

        def dfs(root):
            if not root:
                return
            # 按照 左-打印-右的方式遍历
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res


# Time Comp: O(n), Space Comp: O(h), h is the height of tree
# 递归实现时，是函数自己调用自己，一层层的嵌套下去，操作系统/虚拟机自动帮我们用 栈 来保存了每个调用的函数

# 解法2：迭代. 我们自己用栈来实现上面的递归
class Solution(object):
    def inorderTraversal(self, root):
        res = [] # 创建一个列表用于存储
        stack = [] #创建一个栈
        while stack or root: #当栈不是空的时候 或者是根的时候
            # 不断往左子树方向走，每走一次就将当前节点保存到栈中
            # 这是模拟递归的调用
            if root: # 如果是根，就把根加入到栈里 但是先不打印，然后往左子树走
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()            # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
                res.append(tmp.val)
                root = tmp.right             # 然后转向右边节点，继续上面整个过程
        return res                           # 最后返回列表
