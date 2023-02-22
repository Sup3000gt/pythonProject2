# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head  # 创建一个慢指针指向head
        fast = head  # 创建一个快指针指向head
        while fast and fast.next:  # 当fast和fast.next都不为None的时候
            slow = slow.next  # 慢指针移动1格
            fast = fast.next.next  # 快指针移动2格
            if slow == fast:  # 如果慢指针追上了快指针 返回True,说明列表有循环
                return True
        return False  # 如果跑完循环 还没追上 说明列表没有cycle


"""
解法2：哈希表
遍历所有节点，每次遍历到一个节点时，判断该节点此前是否被访问过
def hasCycle(self, head: ListNode) -> bool:
        seen = set() 创建一个空的哈希表
        while head: 从head开始循环
            if head in seen: 如果这个节点在哈希表中 返回True
                return True
            seen.add(head) 如果不在 那就添加到哈希表中
            head = head.next 然后head向右移动
        return False 如果循环跑完 head == False， 那么说明没有cycle
"""