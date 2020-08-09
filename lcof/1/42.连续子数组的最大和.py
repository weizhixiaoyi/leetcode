# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums_len = len(nums)

        ans = nums[0]
        sum_value = 0
        for i in range(0, nums_len):
            sum_value += nums[i]
            ans = max(ans, sum_value)

            if sum_value < 0:
                sum_value = 0

        return ans


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ans = Solution().maxSubArray(nums)
    print(ans)
