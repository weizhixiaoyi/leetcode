# -*- coding:utf-8 -*-

"""
class MedianFinder:
    def __init__(self):
        self.nums = []
        self.nums_len = 0

    def addNum(self, num: int) -> None:

        # 顺序插入保证插入复杂度为O(n)
        if not self.nums:
            self.nums.append(num)
            self.nums_len += 1
            return
        flag = False
        for i in range(self.nums_len - 1, -1, -1):
            if num >= self.nums[i]:
                self.nums.insert(i + 1, num)
                flag = True
                break
        if flag is False:
            self.nums.insert(0, num)

        self.nums_len += 1
        # print(self.nums)

    def findMedian(self) -> float:
        half_len = self.nums_len // 2
        print(self.nums)
        if self.nums_len % 2 != 0:
            return self.nums[half_len]
        else:
            return (self.nums[half_len - 1] + self.nums[half_len]) / 2
"""

import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []  # 大顶堆, 保存较小的部分
        self.right = []  # 小顶堆, 保存较大的部分
        self.left_len = 0
        self.right_len = 0

    def addNum(self, num: int) -> None:
        if self.left_len == self.right_len:
            heapq.heappush(self.left, -num)
            heapq.heappush(self.right, -heapq.heappop(self.left))
            self.right_len += 1
        else:
            heapq.heappush(self.right, num)
            heapq.heappush(self.left, -heapq.heappop(self.right))
            self.left_len += 1

    def findMedian(self) -> float:
        if self.left_len == self.right_len:
            return (-self.left[0] + self.right[0]) / 2
        else:
            return self.right[0]


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(3)
print(obj.findMedian())
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
param_2 = obj.findMedian()

# nums = []
# heapq.heappush(nums, 1)
# heapq.heappush(nums, 3)
# heapq.heappush(nums, 2)
# nums = [10, 3, 9, 11, 1, 6]
# heapq.heapify(nums)
# print(nums)
# print(nums[0])
# print(heapq.heappop(nums))
