class Node: # 定义一个 单链表 节点的结构体
    def __init__(self, val): # 节点需要的元素 元素的值 和 一个指向 “下一个的” 指针
        self.val = val
        self.next = None


class MyLinkedList: # 开始定义链表

    def __init__(self):
        self.size = 0           # 链表需要 两个元素， 一个是链表的初始长度size，起始值为0
        self.head = Node(0)      # 还有一个就是链表的头部元素， 默认是0

    def get(self, index: int) -> int:           # 获取第index 元素的值 的函数
        if index < 0 or index >= self.size:     # 当index 小于 0 或者 大于 链表的长度时,返回 -1 因为不存在
            return -1
        current = self.head                     # 设置一个指针 指向头部
        for _ in range(index + 1):              # 从头部开始遍历，每次遍历都把指针向右移动一格,直到指针指到index
            current = current.next
        return current.val                      # 返回指针的值


    def addAtHead(self, val: int) -> None:      # 直接调用下面写好的addAtIndex函数, 从 0 开始插入
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:      # 直接调用下面写好的addAtIndex函数，从 self.size开始插入
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:  # 在 index 前面的位置插入元素
        if index > self.size:                            # 如果index > 链表长度 那么不合法, 返回 None
            return None
        self.size += 1                                   # 链表长度 +1
        newNode = Node(val)                              # 创建一个新的newNode
        prev_node = None                                 # 慢指针指向None
        current_node = self.head                         # 快指针 指向头结点
        for _ in range(index + 1):                       # 开始遍历 从0 一直遍历到 index+1的节点
            prev_node = current_node                     # 慢指针 右移
            current_node = current_node.next             # 快指针 右移
        else:                                            # 遍历结束，把慢元素的指针 指向添加的新元素，然后把新元素的指针 指向快指针
            prev_node.next = newNode
            newNode.next = current_node

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:                      # 判定这个index是不是合法的 在0到链表长度之间
            # 计数-1
            self.size -= 1                              # 因为要减少元素， 所以链表长度减1
            prev_node = None                            # 双指针 慢指针指向None, 快指针指向头部
            current_node = self.head
            for _ in range(index + 1):                  # 开始遍历 一直遍历到 index +1 节点
                prev_node = current_node                # 双指针 各右移以为
                current_node = current_node.next
            else:                                       # 直到遍历结束 说明找到了index的位置
                prev_node.next = current_node.next      # 前一个元素的指针(慢指针) 指向 当前元素的下一个元素，跳过当前元素
                current_node.next = None                # 然后把当前元素的指针(快指针)指向None 这个元素就被删除了