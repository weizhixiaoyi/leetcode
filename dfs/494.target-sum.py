# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # 直接进行递归求解会超时, 共pow(2, n)可能性, 因此需要将中间结果进行存储
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < S: return 0
        # 针对num中的数, 每个数据可进行加或者减, 所以最值为[-sum(nums), sum(nums)]

        # dp[i][j]表示i个数组成sum=j的个数
        nums_len = len(nums)
        nums_sum = sum(nums)
        # ...,-,-,-,0,+,+,+...
        t = nums_sum * 2 + 1
        dp = [[0 for j in range(t)] for i in range(nums_len)]
        if nums[0] == 0:
            dp[0][nums_sum] = 2
        else:
            dp[0][nums_sum + nums[0]] = 1
            dp[0][nums_sum - nums[0]] = 1

        # print(dp)
        for i in range(1, nums_len):
            for j in range(0, t):
                l = j - nums[i]
                if l < 0: l = 0
                r = j + nums[i]
                if r >= t: r = t - 1

                dp[i][j] = dp[i - 1][l] + dp[i - 1][r]

        # print(dp)
        return dp[nums_len - 1][nums_sum + S]


if __name__ == '__main__':
    nums = [1]
    S = 2
    ans = Solution().findTargetSumWays(nums, S)
    print('ans: ', ans)

# 暴力法求解会出现超时
"""
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.ans = 0

        def helper(l, this_sum):
            # 递归截止条件
            if len(l) == 0 and this_sum != S:
                return 0

            # 满足条件
            if len(l) == 0 and this_sum == S:
                # print(this_sum)
                return 1

            # 每个数据共两种选择
            # 加法
            if helper(l[1:], this_sum + l[0]):
                self.ans += 1
            # 减法
            if helper(l[1:], this_sum - l[0]):
                self.ans += 1
            return 0

        helper(nums, 0)
        return self.ans
"""
