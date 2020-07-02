# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 0: return 0
        if nums_len == 1: return nums[0]
        if nums_len == 2: return max(nums[0], nums[1])

        nums1 = nums[1:]
        nums2 = nums[0:-1]

        def helper(values):
            # print(values)
            values_len = len(values)
            dp = [0 for i in range(0, values_len)]
            dp[0], dp[1] = values[0], max(values[0], values[1])
            for i in range(2, values_len):
                dp[i] = max(dp[i - 1], dp[i - 2] + values[i])
            # print(dp)
            return dp[-1]

        nums1_max = helper(nums1)
        nums2_max = helper(nums2)
        return max(nums1_max, nums2_max)


if __name__ == '__main__':
    nums = [1, 3, 1, 3, 100]
    ans = Solution().rob(nums)
    print('ans: ', ans)
