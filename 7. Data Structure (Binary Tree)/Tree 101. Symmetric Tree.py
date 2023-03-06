# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 解法1： 递归
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)  # 返回比较的值

    def compare(self, left, right):  # 创建一个比较函数 来比较左右2个子树
        # 首先排除空节点的情况
        if left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        elif left == None and right == None:
            return True
        # 排除了空节点，再排除数值不相同的情况
        elif left.val != right.val:
            return False

        # 此时就是：左右节点都不为空，且数值相同的情况
        # 此时才做递归，做下一层的判断
        outside = self.compare(left.left, right.right)  # 左子树：左、 右子树：右
        inside = self.compare(left.right, right.left)  # 左子树：右、 右子树：左
        # 如果左右都对称就返回true ，有一侧不对称就返回false
        isSame = outside and inside  # 左子树：中、 右子树：中 （逻辑处理）
        return isSame  # 最后把isSame的值返还给compare

        # 还可以用迭代 队列来解， 也可以用迭代 栈来解， 又或者是层次遍历
