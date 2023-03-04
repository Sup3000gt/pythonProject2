# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 二叉树层序遍历迭代解
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        final_results = []  # 最终返回的列表,final_result
        if not root:  # 如果不是root,返回 空列表
            return final_results

        from collections import deque  # import 队列
        que = deque([root])  # 创建一个队列，并且把root也就是根加入到队列里
        while que:  # 循环一直到队列为空
            size = len(que)  # 设一个变量size用来统计当层一共有多少个node,例如起始只有root,size就是1
            temp_result = []  # 设一个局部变量的临时列表 用来统计每一层的node的值
            for _ in range(size):
                                    # When you are not interested in some values returned by a function we
                                    # use underscore in place of variable name
                cur = que.popleft()  # 弹出队列的第一个元素（也就是最左边的元素),并且把弹出的这个元素定义为current
                temp_result.append(cur.val)  # 把弹出的这个元素的值加入到局部变量的列表里
                if cur.left:  # 如果current有左孩子就把左孩子加入到队列里
                    que.append(cur.left)
                if cur.right:  # 如果current也有右孩子就把有孩子加入到队列里面
                    que.append(cur.right)
            final_results.append(temp_result)  # 当这个for loop跑完说明已经遍历完了二叉树当前的一层，
                                               # 那么把一整层的临时列表加入到最终列表中

        return final_results  # 最后返回最终的列表

    # 递归解法
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []        # 创建一个空的列表用来储存
        def eachLevel (root, depth):    # 写一个函数 传入根节点, 树的初始深度为0
            if not root: return []      # 如果根节点为空，返回空列表
            if len(res) == depth:       # 如果最终列表的长度等于树的深度,说明目前一层已经填满 我们需要给新的一层添加新的子列表
                res.append([])
            res[depth].append(root.val) # 然后把节点的值传入子列表
            if root.left:               # 之后递归 左子树， 传入 左节点 并且因为是下一层了 所以depth +1
                eachLevel(root.left,depth+1)
            if root.right:              # 接着 递归右子树
                eachLevel(root.right, depth+1)
        eachLevel(root,0)
        return res                      # 最后输出完整的result 列表
