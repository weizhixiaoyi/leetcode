# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        self.quickSort(0, nums_len - 1, nums)
        return nums

    def quickSort(self, left, right, nums):
        if left >= right: return

        i, j = left, right
        pivot = nums[left]
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i] = nums[j]

            while i < j and nums[i] <= pivot:
                i += 1
            nums[j] = nums[i]
        nums[i] = pivot

        self.quickSort(left, i - 1, nums)
        self.quickSort(i + 1, right, nums)


if __name__ == '__main__':
    nums = [5, 1, 1, 2, 0, 0]
    ans = Solution().sortArray(nums)
    print(ans)
