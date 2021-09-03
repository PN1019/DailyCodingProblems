#This problem was asked by Amazon.

#Implement a stack API using only a heap. A stack implements the following methods:

#push(item), which adds an element to the stack
#pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)
# Recall that a heap has the following operations:

#push(item), which adds a new key to the heap
# pop(), which removes and returns the max value of the heap
# Solution:
class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.max_stack or val > self.stack[self.max_stack[-1]]:
            self.max_stack.append(len(self.stack) - 1)

    def pop(self):
        if not self.stack:
            return None
        if len(self.stack) - 1 == self.max_stack[-1]:
            self.max_stack.pop()

        return self.stack.pop()

    def max(self):
        if not self.stack:
            return None
        return self.stack[self.max_stack[-1]]


s = Stack()
s.push(1)
s.push(3)
s.push(2)
s.push(5)
assert s.max() == 5
s.pop()
assert s.max() == 3
s.pop()
assert s.max() == 3
s.pop()
assert s.max() == 1
s.pop()
assert not s.max()

s = Stack()
s.push(10)
s.push(3)
s.push(2)
s.push(5)
assert s.max() == 10
s.pop()
assert s.max() == 10
s.pop()
assert s.max() == 10
s.pop()
assert s.max() == 10
s.pop()
assert not s.max()
