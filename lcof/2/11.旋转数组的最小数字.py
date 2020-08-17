# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        nums = numbers
        nums_len = len(nums)
        left, right = 0, nums_len - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right = right - 1

        return nums[left]


if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    ans = Solution().minArray(nums)
    print(ans)
