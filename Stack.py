#Stack in Python can be implemented using the following ways:
#list
#Collections.deque
#queue.LifoQueue
stack = []
# append() function to push
# element in the stack
stack.append('a')
# pop() function to pop
# element from stack in
# LIFO order
print(stack.pop())



from collections import deque

stack = deque()
stack.append('a')

from queue import LifoQueue

# Initializing a stack
stack = LifoQueue(maxsize=3)

# qsize() show the number of elements
# in the stack
print(stack.qsize())

# put() function to push
# element in the stack
stack.put('a')

#stack.peek() 查看peek of the stack
#stack.size() 查看 stack 的size
#stack.isEmpey() 查看是否为空
class Stack:
  def __init__(self):
    self.__index = []

  def __len__(self):
    return len(self.__index)

  def push(self,item):
    self.__index.insert(0,item)

  def peek(self):
    if len(self) == 0:
      raise Exception("peek() called on empty stack.")
    return self.__index[0]

  def pop(self):
    if len(self) == 0:
      raise Exception("pop() called on empty stack.")
    return self.__index.pop(0)

  def __str__(self):
    return str(self.__index)

Stack()
Stack.push("1")
