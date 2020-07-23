# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        zero_num = 0
        if nums[0] == 0: zero_num += 1
        for i in range(1, len(nums)):
            if nums[i] == 0:
                zero_num += 1
                continue
            if nums[i] == nums[i - 1]:
                return False

        nums = nums[zero_num:]
        nums_len = len(nums)
        # print(zero_num, nums, nums_len)
        diff = 0
        for i in range(1, nums_len):
            if nums[i] - nums[i - 1] == 1:
                continue
            else:
                diff += nums[i] - nums[i - 1] - 1
        if zero_num - diff >= 0:
            return True
        else:
            return False


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    # nums = [0, 0, 1, 6, 5]
    # nums = [0, 0, 1, 2, 5]
    # nums = [0, 0, 8, 5, 4]
    ans = Solution().isStraight(nums)
    print(ans)
