# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums: return 0
        s = S
        nums_len = len(nums)
        nums_sum = sum(nums)
        if (nums_sum + s) % 2 != 0 or s > nums_sum:
            return 0

        x = (nums_sum + s) // 2
        dp = [0 for i in range(x + 1)]
        dp[0] = 1
        for i in range(nums_len):
            for j in range(x, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]

        return dp[x]


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    S = 3
    ans = Solution().findTargetSumWays(nums, S)
    print(ans)
