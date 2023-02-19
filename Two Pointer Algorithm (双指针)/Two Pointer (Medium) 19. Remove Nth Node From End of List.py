# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)     # 创建一个虚拟节点 pointer指向头部head
        slow = dummy                    # 创立 2个指针 一个快一个慢 都指向 虚拟节点
        fast = dummy
        while (n != 0):                 # 当n 不等于零的时候 快指针右移, n-1, 循环到 快指针移动n次为止,这时慢指针还在起点
            fast = fast.next
            n -= 1
        while (fast.next!=None ):       # 第一个循环结束之后,继续移动快指针直到快指针指向None也就是链表的最后一个元素
            fast = fast.next            # 这次我们 快慢指针 一起移动, 当快指针移动到链表最后一个元素的时候
            slow = slow.next            # 慢指针指向的下一个元素 就是我们需要删除的倒数第n个元素
        slow.next = slow.next.next      # 那么把慢指针.next 指向慢指针.next.next 这样这个元素就删除了
        return dummy.next                 # 之后我们返还 虚拟节点 *注意* 因为节点是虚拟的 所以要返还dummy.next