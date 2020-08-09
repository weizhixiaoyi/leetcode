# -*- coding:utf-8 -*-


class MaxQueue:
    def __init__(self):
        self.nums = []
        self.max_nums = []

    def max_value(self) -> int:
        if not self.max_nums: return -1
        return self.max_nums[0]

    def push_back(self, value: int) -> None:
        self.nums.append(value)
        while self.max_nums and self.max_nums[-1] < value:
            self.max_nums.pop()
        self.max_nums.append(value)

    def pop_front(self) -> int:
        if not self.nums: return -1

        front = self.nums[0]
        self.nums = self.nums[1:]
        if front == self.max_nums[0]:
            self.max_nums = self.max_nums[1:]
        return front


# Your MaxQueue object will be instantiated and called as such:
obj = MaxQueue()
param_1 = obj.max_value()
print(param_1)
obj.push_back(3)
param_3 = obj.pop_front()
print(param_3)
