# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 解法1 递归
        def isOrNot(root, targetSum):
            # 设定返回值
            if (not root.left) and (not root.right) and (targetSum == 0):
                return True  # 遇到叶子节点，并且计数为0，返回True
            if (not root.left) and (not root.right):
                return False  # 遇到叶子节点，计数不为0，返回False
            if root.left:
                targetSum -= root.left.val  # 左节点
                if isOrNot(root.left, targetSum):  # 递归，处理左节点
                    return True
                targetSum += root.left.val  # 回溯
            if root.right:
                targetSum -= root.right.val  # 右节点
                if isOrNot(root.right, targetSum):  # 递归，处理右节点
                    return True
                targetSum += root.right.val  # 回溯
            return False

        if root == None:
            return False  # 处理掉空treeNode
        else:
            return isOrNot(root, targetSum - root.val)


""" 
    这是递归的精简写法，这个写法是从root开始加上去 看到叶子节点的时候 总和是不是等于目标值
        class Solution:
            def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
                def dfs(root, currSum):
                    if not root:  如果参数不是root 直接返回False
                        return False
                    currSum += root.val 如果参数是root 那么就把root的值添加到currentSum里
                    if not root.left and not root.right: 如果没有左右孩子 说明是叶子节点了
                        return currSum == targetSum 判定 从根一直加到叶子节点 是否等于目标值，如果是就是True,不然就是False

                    return (dfs(root.left, currSum) or dfs(root.right, currSum)) 递归来分别处理左子树和右子树

                return dfs(root, 0) 最后返回 函数dfs(root,currSum 因为currSum初始值是0)
   
    这也是精简写法 这个写法是从root开始到叶子 一直减下去 看最后叶子节点的值是否等于剩余值
    class Solution(object):
    def hasPathSum(self, root, sum):
        if not root: 如果参数不是root 直接返回False
            return False
        if not root.left and not root.right: 如果没有左右孩子 说明是叶子节点了 直接判定sum 是否等于root.val
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        最后递归里面的参数 分别是 左右的子树 和 sum-root.val

                
"""
