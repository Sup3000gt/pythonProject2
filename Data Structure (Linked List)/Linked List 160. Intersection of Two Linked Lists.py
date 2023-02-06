# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA , lenB = 0 , 0                # 先分别求出2个链表的长度
        curr = headA
        while (curr != None):              # 当链表不为空时， 指针右移 计数器加一
            lenA += 1
            curr = curr.next

        curr = headB
        while (curr != None):
            lenB += 1
            curr = curr.next

        currA , currB = headA , headB       # 双指针

        if lenA > lenB:                     # 让currB变成最长链表的头部,此处需要选择一个链表固定为更长的那一个
            currA , currB = currB , currA
            lenA , lenB = lenB , lenA

        for _ in range(lenB - lenA):        # 因为这里我们要选择长的那个链表让指针先跑
            currB = currB.next              # 让长链表的指针先跑 链表A和链表B的 GAP的长度

        while currA:                        # 然后开始移动短链表的指针
            if currA == currB:              # 如果和 长链表指针一样 那么 返回 任意一个指针即可
                return currA
            else:                           # 如果不是，那么长链表和短链表的指针同时右移一格比较下一个数字
                currA = currA.next
                currB = currB.next
        return None                         # 最后 如果遍历结束都没有 那么返回None值


    # 解法二：
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA = headA    # 指针A 指向A链表头部
        curB = headB    # 指针B 指向B链表头部

        while curA != curB:                                 # 当A和B指针指向不同的值的时候
            curA = headB if curA == None else curA.next     # 如果 链表还没空，就把指针右移一格
            curB = headA if curB == None else curB.next     # 如果链表空了 那么就把指针指向另一个链表的头部

        return curA                                         # 最后返还curA的位置，如果while没跑完就结束 说明找到相交了跳出循环
                                                            # 返还位置， 如果 循环跑完 那么curA就等于None 返回没有相交





