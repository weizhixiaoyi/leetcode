# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_len = len(cost)
        dp = [0 for i in range(cost_len)]

        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, cost_len):
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
        return min(dp[-1], dp[-2])


if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    ans = Solution().minCostClimbingStairs(cost)
    print(ans)
