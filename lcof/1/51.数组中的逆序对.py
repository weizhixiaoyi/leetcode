# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        nums_len = len(nums)

        self.ans = 0
        temp = [0 for i in range(nums_len)]
        self.sort(nums, 0, nums_len - 1, temp)
        return self.ans

    def sort(self, nums, left, right, temp):
        if left >= right: return None
        mid = (left + right) // 2
        self.sort(nums, left, mid, temp)
        self.sort(nums, mid + 1, right, temp)
        self.merge(nums, left, mid, right, temp)

    def merge(self, nums, left, mid, right, temp):
        i, j = left, mid + 1
        t = 0

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp[t] = nums[i]
                i += 1
                t += 1
            else:
                temp[t] = nums[j]
                j += 1
                t += 1
                self.ans += (mid - i + 1)
        while i <= mid:
            temp[t] = nums[i]
            i += 1
            t += 1
        while j <= right:
            temp[t] = nums[j]
            j += 1
            t += 1

        nums[left: right + 1] = temp[0: t]


if __name__ == '__main__':
    nums = [7, 5, 6, 4]
    # nums = [1, 3, 2, 3, 1]
    ans = Solution().reversePairs(nums)
    print(ans)
