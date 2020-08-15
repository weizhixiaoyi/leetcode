# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 0 or nums_len == 1: return 0

        self.ans = 0
        tmp = [0 for i in range(nums_len)]
        self.sort(0, nums_len - 1, nums, tmp)
        # print(nums)
        return self.ans

    def sort(self, left, right, nums, tmp):
        if left >= right: return

        mid = (left + right) // 2
        self.sort(left, mid, nums, tmp)
        self.sort(mid + 1, right, nums, tmp)
        self.merge(left, mid, right, nums, tmp)

    def merge(self, left, mid, right, nums, tmp):
        i, j, k = left, mid + 1, 0

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                tmp[k] = nums[i]
                i += 1
                k += 1

            if nums[i] > nums[j]:
                tmp[k] = nums[j]
                j += 1
                k += 1
                self.ans += (mid - i + 1)

        while i <= mid:
            tmp[k] = nums[i]
            i += 1
            k += 1
        while j <= right:
            tmp[k] = nums[j]
            j += 1
            k += 1
        nums[left: right + 1] = tmp[0:k]


if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5, 6, 8, 7]
    nums = [1, 3, 2, 3, 1]
    ans = Solution().reversePairs(nums)
    print(ans)
