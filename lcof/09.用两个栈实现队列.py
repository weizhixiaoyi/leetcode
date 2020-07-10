# -*- coding:utf-8 -*-

class CQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2 == []:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

            if self.stack2:
                return self.stack2.pop()
            else:
                return -1

        return self.stack2.pop()


if __name__ == '__main__':
    # Your CQueue object will be instantiated and called as such:
    obj = CQueue()
    obj.appendTail(1)
    param_2 = obj.deleteHead()
    print(param_2)
