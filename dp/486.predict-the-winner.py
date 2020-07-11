# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        if nums_len == 0 or nums_len == 1: return True

        # dp[i][j]表示nums从i到j中, 先手比后手多的数值
        dp = [[0 for j in range(nums_len)] for i in range(nums_len)]
        for i in range(nums_len): dp[i][i] = nums[i]

        for i in range(nums_len - 1, -1, -1):
            for j in range(i + 1, nums_len):
                # print(i, j)
                dp[i][j] = max(nums[i] + (-dp[i + 1][j]), nums[j] + (-dp[i][j - 1]))

        # print(dp)
        if dp[0][nums_len - 1] >= 0:
            return True
        else:
            return False


if __name__ == '__main__':
    nums = [1, 5, 2]
    ans = Solution().PredictTheWinner(nums)
    print(ans)
