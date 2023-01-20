# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)  # 在链表头部前,创建一个dummy节点
        curr = head  # 创建一个current指针指向head
        prev = dummy  # 创建一个previous指针 指向dummy
        while curr:  # 从current
            if curr.val == val:  # 如果current当前的指针是我们想要删除的元素val, 那么把previous的指针指向current的下一个元素
                prev.next = curr.next
            else:  # 如果不是previous指针往右移到current指针
                prev = curr

            curr = curr.next  # current指针往右移动 到next

        return dummy.next  # 最后因为dummy是我们自己创建的临时节点，所以注意 我们需要返回的是dummy的下一个节点也就是 dummy.next