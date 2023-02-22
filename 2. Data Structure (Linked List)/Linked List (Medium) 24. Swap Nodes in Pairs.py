# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = ListNode(next=head)            # 创建一个虚拟节点,这个节点的下一个是头结点.也就是在头结点前面创建
        pre = res                            # 建立一个指针 指向这个虚拟节点

        # 必须有pre的下一个和下下个才能交换，否则说明已经交换结束了
        while pre.next and pre.next.next:
            cur = pre.next                  # cur指向虚拟节点的下一个节点， 头结点，也就是test case 的 1
            post = pre.next.next            # post 指向虚拟节点的下下个节点， 也就是test case的 2

            # pre，cur，post对应最左，中间的，最右边的节点
            cur.next = post.next            # 然后把1 原本指向2的Pointer 指向2的下一个也就是3
            post.next = cur                 # 之后把2 原本指向3的pointer 指向回cur也就是 2
            pre.next = post                 # 之后把指向1 的指针 指向2，那么现在的顺序就变成了 虚拟节点 → 2 → 1 → 3，
                                            # 这样我们就完成了1 和 2 的交换
            pre = pre.next.next             # 之后我们把我们指向虚拟节点的指针pre 右移2格 也就是指向3, 然后从新循环
        return res.next                     # 注意 最后我们要返还的是res.next, 而不是pre.next 因为Pre是指针，在我们循环的过程中
                                            # 已经变动了, 这也是为什么开头要建立一个指针pre 指向res 而不是直接用res
