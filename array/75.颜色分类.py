# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        f0, f1, f2 = 0, 0, len(nums) - 1
        while f1 <= f2:
            if nums[f1] == 0:
                nums[f0], nums[f1] = nums[f1], nums[f0]
                f0 += 1
                f1 += 1
            elif nums[f1] == 1:
                f1 += 1
            elif nums[f1] == 2:
                nums[f1], nums[f2] = nums[f2], nums[f1]
                f2 -= 1
        # print(nums)


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    # nums = [2, 2, 1, 1, 0, 2, 0, 0, 1, 2, 1]
    Solution().sortColors(nums)
