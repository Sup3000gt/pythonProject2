# Tree represents the nodes connected by edges. It is a non-linear data structure. It has the following properties
# One node is marked as Root node. 一个节点是根节点
# Every node other than the root is associated with one parent node. 除了根节点以外都有父节点
# Each node can have an arbitrary number of child node. 每个节点都可以有多个子节点


# Depth of the Tree 树的深度 任意一个节点到根部的距离 距离根越远，深度越高 （从1开始）
# 求深度用前序遍历
#       一棵树高度就是他的最大深度
# Height of the Tree 树的高度 从叶子节点到根部的距离 （从1开始）
# 求高度用后序遍历

# 用数组来存储二叉树如何遍历的呢？
# 如果父节点的数组下标是 i，那么它的左孩子就是 i * 2 + 1，右孩子就是 i * 2 + 2。
# 但是用链式表示的二叉树，更有利于我们理解，所以一般我们都是用链式存储二叉树。

# 树的种类
# Binary Tree 二叉树，二叉树是每个节点最多有两个子树的树结构
        # 二叉树特点：
            # 每个结点最多有两颗子树
            # 左子树和右子树是有顺序的，次序不能任意颠倒
            # # 即使树中某结点只有一棵子树，也要区分它是左子树还是右子树
            #                  1
            #                 / \
            #                2   3
            #               / \
            #              4   5

# Full Binary Tree  满二叉树 ---- 除最后一层无任何子节点外，每一层上的所有结点都有两个子结点的二叉树
        # 满二叉树特点：
            # 叶子只能出现在最下一层。出现在其它层就不可能达成平衡
            # 非叶子结点的度(结点拥有的子树数目称为结点的度)一定是2
            # 在同样深度的二叉树中，满二叉树的结点个数最多，叶子数最多
            # 也可以说深度为k，有2^k-1个节点的二叉树
            #                      1
            #                     / \
            #                    2   3
            #                   / \ / \
            #                  4  5 6  7

# Complete Binary Tree 完全二叉树 ---- 除最后一层外，每一层上的结点数均达到最大值；在最后一层上只缺少右边的若干结点
        # 完全二叉树特点：
            # 叶子结点只能出现在最下层和次下层。
            # 最下层的叶子结点集中在树的左部。
            # 倒数第二层若存在叶子结点，一定在右部连续位置。
            # 如果结点度为1，则该结点只有左孩子，即没有右子树。
            # 同样结点数目的二叉树，完全二叉树深度最小
            #
            #                      1
            #                     / \
            #                    2   3
            #                   / \ /
            #                  4  5 6

# Binary Search Tree 二叉搜索树（二叉排序树、二叉查找树）
        # 二叉搜索树特点：
            # 若它的左子树不空，则左子树上的所有结点的值均小于根节点的值
            # 若它的右子树不空，则右子树上的所有结点的值均大于根节点的值
            # 左右子树分别为二叉排序树
            #                      5
            #                     / \
            #                    2   7
            #                   / \ / \
            #                  1  4 6  8

# Structure of Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.left = None  # left child 左孩子
        self.right = None  # right child 右孩子
        self.data = data  # Root node 根节点

    def setData(self, data=None):
        self.data = data  # set data

    def getData(self):
        return self.data  # get data

    def getLeft(self):
        return self.left  # get left child of node

    def getRight(self):  # get right child of node
        return self.right
# Basic operation of Tree 树的基本操作
        # Inserting element 插入元素
        # Deleting element 删除元素
        # Searching for an element 查找元素
        # Traversing the tree 树的遍历

                # 三种最常用的遍历  DFS（深度优先搜索）                Time complexity/Space complexity for all 3 are O(n)
                    # Pre-order Traversal 前序遍历
                        # 先访问根节点，然后递归的前序访问左子树，然后前序访问右子树
                    # In-order Traversal 中序遍历
                        # 先递归的中序访问左子树，然后根节点，最后中序访问右子树
                    # Post-order Traversal 后序遍历
                        # 先递归的后序访问左子树，再后序访问右子树，最后访问根节点

                # 一种单独的遍历   BFS（广度优先搜索）
                    # Level Order Traversal 层次遍历 广度优先搜索（BFS）


# Auxiliary operation of Tree
        # Finding the size of tree
        # Finding the height of tree
        # Finding the level which has maximum sum
        # Finding the least common ancestor(祖先)(LCA) for a given pair of nodes, and many more.

    def insert(self, data):  # 在树里插入数据
        # Compare the new value with the parent node
        if self.data:  # 首先检查当前节点是否有数据，如果有，将新值与父节点进行比较
            if data < self.data:  # 新值小于父节点的值，并且左子树为空，则将其插入左子树
                if self.left is None:
                    self.left = BinaryTreeNode(data)
                else:
                    self.left.insert(data)  # 如果新值小于父节点，但是左子树不是空的,那么用递归决定把这个值插入子树的左子树或者右子树
            elif data > self.data:  # 如果新值大于父节点的值，并且右子树为空，则将其插入右子树
                if self.right is None:
                    self.right = BinaryTreeNode(data)
                else:
                    self.right.insert(data)  # 如果新值小于父节点，但是左子树不是空的,那么用递归决定把这个值插入子树的左子树或者右子树
        else:  # 如果根为空，那就将数据插入根
            self.data = data


