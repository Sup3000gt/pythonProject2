# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 设置一个指针current 指向 head
        current = head
        # 当current 和 current 两个只要有一个不存在 说明链表已经到尾了
        while current != None and current.next != None:
            if current.val == current.next.val:  # 如果current的值和current下一个的值一样说明重复了
                current.next = current.next.next  # 那么将current的指针直接指向下一个的下一个， 这样就可以跳过重复的node
            else:
                current = current.next              #如果不相等 那么指向下一个node 继续循环
        return head  # 最后返回 head 头部节点

    # Time complexity O(n)
