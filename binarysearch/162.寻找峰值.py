# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = list(map(float, nums))
        nums.insert(0, float('-inf'))
        nums.append(float('-inf'))
        nums_len = len(nums)
        left, right = 0, nums_len - 1
        while left < right:
            mid = (left + right) // 2
            # print(mid, nums[mid], nums[mid + 1])
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left - 1


if __name__ == '__main__':
    # nums = [1, 2, 3, 1]
    nums = [1, 2, 1, 3, 5, 6, 4]
    ans = Solution().findPeakElement(nums)
    print(ans)
