# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    #     days_len = len(days)
    #     if days_len == 0: return 0
    #     if days_len == 1: return costs[0]
    #
    #     days = set(days)
    #     durations = [1, 7, 30]
    #
    #     import functools
    #     @functools.lru_cache(None)
    #     def helper(day):
    #         if day > 365:
    #             return 0
    #         elif day in days:
    # return min(helper(day + d) + c for c, d in zip(costs, durations))
    # else:
    #     return helper(day + 1)
    #
    # return helper(1)

    # 首先应该想到定义的状态是什么, 然后再去找状态方程.
    # 通常情况下, 都是问什么就定义状态
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_len = len(days)
        if days_len == 0: return 0
        if days_len == 1: return costs[0]

        max_day = days[-1]
        dp = [0 for i in range(max_day + 1)]  # 表示第i天的最小花费
        idx = 0
        for k in range(1, max_day + 1):
            if k == days[idx]:
                d1 = dp[max(k - 1, 0)] + costs[0]
                d7 = dp[max(k - 7, 0)] + costs[1]
                d30 = dp[max(k - 30, 0)] + costs[2]
                dp[k] = min(d1, d7, d30)
                idx += 1
            else:
                dp[k] = dp[k - 1]
        # print(dp)
        return dp[-1]


if __name__ == '__main__':
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    costs = [2, 7, 15]
    # days = [1, 4, 6, 7, 8, 20]
    # costs = [2, 7, 15]
    ans = Solution().mincostTickets(days, costs)
    print(ans)
