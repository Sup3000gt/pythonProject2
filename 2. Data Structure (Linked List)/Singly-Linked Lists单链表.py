# Node of s singly Linked List 一个空节点自带的属性
class Node:
    # Constructor 起始值为None,下一个节点next也是None
    def __init__(self):
        self.data = None
        self.next = None

    # Method for setting the data field of the Node 为这个节点赋值
    def setData(self, data):
        self.data = data

    # Method for getting the data field of the Node 返回这个节点的值
    def getData(self):
        return self.data

    # Method for setting the Next field of the Node 为下一个节点赋值
    def setNext(self, data):
        self.next = next

    # Method for getting the Next field of the Node 返回下一个节点的值
    def getNext(self):
        return self.next

    # Return True if the node points to another node 查看当前node是不是尾部node
    def hasNext(self):
        return self.next != None

    # check the lenght of list 查看链表的长度
    def length(self):
        current = self.head  # 当前指针设置为链表头部，计数器为0
        count = 0
        while current != None:  # 当链表头部指向值不是None的情况下，计数器加一，指针加一
            count += 1
            current = current.getNext()
        return count

    # Time Comp : O(n) Space Comp : O(1)
    #################################################################################################################
    # insert a Node at Beginning 在头部插入新节点
    def insertAtBeginning(self, data):
        newNode = Node()  # 设置一个新的空节点
        newNode.setData(data)  # 给空节点赋值
        if self.length == 0:  # if self.length == 0, 说明这个链表是空的
            self.head = newNode  # 那么把这个新的node 设置为链表头
        else:
            newNode.setNext(self.head)  # 不然就把这个新的node指针指向下一个node
            self.head = newNode  # 然后把头部指针指向这个新node
        self.length += 1  # 然后链表的长度加一

    # insert a Node at End 在尾部插入新节点
    def insertAtEnd(self, data):
        newNode = Node()  # 设置一个新的空节点
        newNode.setData(data)  # 给空节点赋值
        current = self.head  # 设置current 指针 指向链表头部
        while current.getNext() != None:  # 当current的下一个node不等于None,说明这不是最后一个节点，那么就把指针往后移动
            current = current.getNext()
        current.setNext(newNode)  # 当指针无法移动时，说明current的指针就是最后一个node，那么把最后一个node的指针指向newnode
        self.length += 1  # 链表长度加一

    # insert a Node at middle 在pos的位置（非头和尾）插入
    def insertAtPos(self, pos, data):
        if pos > self.length or pos < 0:  # 如果pos大于列表长度或者小于0,那么返回None
            return None
        else:
            if pos == 0:  # 如果 pos ==0，那么说明插入位置是头部，直接调用头部插入的method
                self.insertAtBeginning(data)
            else:
                if pos == self.length:  # 如果pos ==链表的长度，那么说明插入位置是尾部,直接调用尾部插入method
                    self.insertAtEnd(data)
                else:  # 如果以上2个都不是，那么则插入在中间某个位置
                    newNode = Node()  # 创建新节点，并且为新节点赋值
                    newNode.setData(data)
                    count = 0  # 设置计数器为0
                    current = self.head  # current指针为头部节点
                    while count < pos - 1:  # 当计数器小于我们想插入的位置的前一个节点时，计数器加一，current指针往右移动一格
                        count += 1
                        current = current.getNext()
                    newNode.setNext(current.getNext())  # 当循环完毕时，我们current的指针应该在pos-1的节点，
                    # 把新节点的指针指向当前node的指针的方向
                    # 例如我们想插入的位置是4, 那么current应该指向3
                    current.setNext(newNode)  # 然后再把当前node的指针 指向新节点
                    self.length += 1  # 链表长度+1

    # Time Complexity: O(n), since for worst case, we may need to insert the node at the end of the list
    # Space Complexity: O(1), for creating one temp variable
    ####################################################################################################################
    # Delete first node in the singly-linked list 从头部删除
    def deleteFromBeginning(self):
        if self.length() == 0:  # 如果链表长度为0，返回 "这是一个空链表"
            return "This list is empty"
        else:  # 反之 头部指针指向下一个node,并设置为头部节点
            self.head = self.head.getNext()
            self.length -= 1  # 链表长度-1

    # delete the last node in the singly-linked list 从尾部删除
    def deleteLastNode(self):
        if self.length() == 0:  # 如果链表长度为0，返回 "这是一个空链表"
            return "This list is empty"
        else:
            currentNode = self.head  # 设置2个指针 都指向 链表头部
            previousNode = self.head
            while currentNode.getNext() != None:  # currentNode.getNext() 如果等于None,说明这个链表只有一个头节点，那么跳出循环
                previousNode = currentNode  # previousNode指向currentNode
                currentNode = currentNode.getNext()  # currentNode指向 下一个Node 一直循环到currentNode == last Node为止
            previousNode.setNext(None)  # 直接把previousNode指向下一个Node的指针设置为None,这样原本后面的currentNode就会丢失也就被删除了
            self.length -= 1  # 链表长度-1

    # Delete middle node in singly_linked list 从链表的中间删除元素
    # In this case the node removed is always located between two nodes. Head and tail are not updated in this case
    def deleteFromMiddle(self,node):
        if self.length == 0: #如果length ==0 ,返回空列表
            raise ValueError("List is empty")
        else: #设置2个指针，current = 头元素 ，previous = None, found = False
            current = self.head
            previous = None
            found = False
            while not found:
                if current == node: #如果current == node ,找到目标 跳出循环
                    found = True
                elif current is None: #循环完毕 找不到目标，返回 目标不在列表中
                    raise ValueError("Node not in Linked List")
                else: #privious和current的指针都往右移动
                    previous = current
                    current = current.getNext()
        if previous is None: #如果previous的值是None
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.length -= 1
