# 解决双指针问题三种常用思想：

    # 左右指针：需要两个指针，一个指向开头，一个指向末尾，然后向中间遍历，直到满足条件或者两个指针相遇
        # 代表题目
            # 167. Two Sum II
            # 15. 3Sum
            # 16. 3Sum Closest
            # 18. 4Sum
            # 11. Container With Most Water

    # 快慢指针：需要两个指针，开始都指向开头，根据条件不同，快指针走得快，慢指针走的慢，直到满足条件或者快指针走到结尾
        # 代表题目
            # 27. Remove Element
            # 283. Move Zeroes
            # 26. Remove Duplicates from Sorted Array
            # 80. Remove Duplicates from Sorted Array II
            # 287. Find Duplicate Number

    # 后序指针：常规指针操作是从前向后便利，对于合并和替换类型题，防止之前的数据被覆盖，双指针需从后向前便利
        # 代表题目
            # 88. Merge Sorted Array

    # 记忆口诀：左右指针中间夹，快慢指针走到头，后序指针往回走

# 双指针法将时间复杂度：O(n^2)的解法优化为 O(n)的解法。也就是降一个数量级，题目如下：
                    # 27.移除元素
                    # 15.三数之和
                    # 18.四数之和

    # 链表相关双指针题目：
                    # 206.反转链表
                    # 19.删除链表的倒数第N个节点
                    # 160.链表相交
                    # 142.环形链表II
