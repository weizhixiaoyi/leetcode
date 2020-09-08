# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums_len = len(nums)
        left, right = 0, nums_len - 1
        while left < right:
            mid = (left + right) // 2
            # print(left, mid, right)
            if nums[mid] > nums[right]:
                left = mid + 1
            if nums[mid] < nums[right]:
                right = mid
        # print(left)
        return nums[left]


if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    ans = Solution().findMin(nums)
    print(ans)
