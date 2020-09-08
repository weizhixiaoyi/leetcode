# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums_len = len(nums)
        left, right = 0, nums_len - 1
        while left < right:
            mid = (left + right) // 2
            # print(left, mid, right)
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[right]:
                right = right - 1
        return nums[left]


if __name__ == '__main__':
    nums = [2, 2, 2, 0, 1]
    # nums = [3, 1, 3]
    ans = Solution().findMin(nums)
    print(ans)
