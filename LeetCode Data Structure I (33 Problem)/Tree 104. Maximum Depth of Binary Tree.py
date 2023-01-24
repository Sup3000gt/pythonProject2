# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getHeight(root): # 用后序遍历 来实现的递归
            if root == None: #如果 root是空 返回0
                return 0
            leftHeight = getHeight(root.left)       # 左子树递归
            rightHeight = getHeight(root.right)     # 右子树递归
            height = 1+max(leftHeight,rightHeight)  # 比较左右子树返回值取大的那个 然后+1
            return height                           # 最后返回最终值
        return getHeight(root)

                    # 上面三行代码可以精简成一行
                    # return 1 + max(self.maxdepth(root.left), self.maxdepth(root.right)
                    # 这也是用的递归 只不过是精简版

    # 如果用迭代法来写，那么就使用层序遍历
    import collections
    class solution:
        def maxdepth(self, root: treenode) -> int:
            if not root: #如果None 返回0
                return 0
            depth = 0                               # 创建一个变量depth 记录深度
            queue = collections.deque()             # 创建一个队列
            queue.append(root)                      # 把根部添加到队列里面
            while queue:                            # 当队列不为空的时候
                size = len(queue)                   # 创建一个变量来记录每层队列的长度
                depth += 1                          # 每一次循环 深度+1
                for i in range(size):               # 内循环 循环队列的长度
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return depth                            # 最后返回深度


