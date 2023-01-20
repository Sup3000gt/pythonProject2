# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 解法1： iteration
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)  # 设置一个dummy Node
        previous = dummy  # 设置一个前指针 previous 指向 dummy Node
        while list1 and list2:  # 当list1和list2都不为None的时候
            if list1.val < list2.val:  # 如果list1的节点比较小
                previous.next = list1  # 那么就把dummy的指针指向list1
                list1 = list1.next  # 然后list1 往右移动
            else:
                previous.next = list2  # 不然就把指针指向list2 然后list2右移
                list2 = list2.next
            previous = previous.next  # previous指针右移也就是移动到list1.val或者list2.val上面
        if list1 is not None:  # 如果循环结束了 说明list1和list2肯定有1个空了
            previous.next = list1  # 如果list 不是None,那么就把previous的指针指向list1
        else:
            previous.next = list2  # 反之，则指向list2
        return dummy.next  # 最后因为dummy是我们建立的临时的node,所以不要直接返回dummy,要返回dummy.next


# 解法2 Recursion
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:  # 如果list1空了 返回list2
            return list2
        elif list2 is None:  # 如果list2空了，返回list1
            return list1
        elif list1.val < list2.val:  # 如果list1的第一个元素小于list2的第一个元素
            list1.next = self.mergeTwoLists(list1.next, list2)  # list1的下一个元素继续执行mergeTwoLists
            return list1
        else:  # 反之list2继续执行
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
