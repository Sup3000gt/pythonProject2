# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 遍历所有节点，每次遍历到一个节点时，判断该节点此前是否被访问过

        seen = set()                # 创建一个空的set
        while head:                 # 从head开始循环
            if head in seen:        # 如果这个节点在哈希表中 返回True
                return head
            seen.add(head)          # 如果不在 那就添加到哈希表中
            head = head.next        # 然后head向右移动
        return None                 # 如果循环跑完 head == False， 那么说明没有cycle