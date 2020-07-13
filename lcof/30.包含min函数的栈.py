# -*- coding:utf-8 -*-

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
print(obj.min())
obj.pop()
# print(obj.top())
print(obj.min())
