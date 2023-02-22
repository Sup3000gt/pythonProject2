# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 方法1：Iteration (迭代)
        if not root: #如果不是根节点 直接返回[]
            return []
        stack = [root] #新建一个栈, root = [1,null,2,3]
        result = []    #建立一个list用于存储数据
        while  stack: #当stack不为空的时候
            node = stack.pop() #访问根节点，直接进行操作(输出到数组) 注意：node = stack.pop()会把stack里面的root弹出去
            result.append(node.val)
            if node.right:      # 先入栈右节点
                stack.append(node.right)
            if node.left:       # 后入栈左节点，这样下一轮循环先访问左节点，维护了访问顺序
                stack.append(node.left)
        return result       # 最后返回 result

    # 方法2:递归
    # 中序遍历：打印 - 左 - 右
    # 终止条件：当前节点为空时
    # 函数内：递归的调用左节点，打印当前节点，再递归调用右节点
    class Solution:
        def preorderTraversal(self, root: TreeNode) -> List[int]:
            def preorder(root: TreeNode): # 打印 -- 左 -- 右 的方式遍历
                if not root:
                    return
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)

            res = list()
            preorder(root)
            return res

