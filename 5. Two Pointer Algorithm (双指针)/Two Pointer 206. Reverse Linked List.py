# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 设置2个node,pre 和 current. pre 指向None 代表, current指向head。
        pre = None
        current = head
        while current: #遍历整个链表
            tmp = current.next #记录当前节点的下一个节点
            current.next = pre #然后将原本指向下一个节点的指针 指向前一个节点pre
            pre = current #然后把pre和current都右移一格
            current = tmp
        return pre