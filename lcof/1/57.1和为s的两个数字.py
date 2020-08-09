# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        i, j = 0, nums_len - 1
        while i <= j:
            cur_sum = nums[i] + nums[j]
            if cur_sum == target:
                return [nums[i], nums[j]]
            if cur_sum < target:
                i += 1
            if cur_sum > target:
                j -= 1


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    ans = Solution().twoSum(nums, target)
    print(ans)
