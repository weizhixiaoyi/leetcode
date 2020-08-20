# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     prices_len = len(prices)
    #     if prices_len < 2: return 0
    #     self.ans = 0
    #
    #     def dfs(idx, state, cur_profit):
    #         if idx == prices_len:
    #             # print(cur_profit)
    #             self.ans = max(self.ans, cur_profit)
    #             return
    #
    #         # 继续保持下去
    #         dfs(idx + 1, state, cur_profit)
    #
    #         # 状态改变
    #         if state == 0:
    #             dfs(idx + 1, 1, cur_profit - prices[idx])
    #         else:
    #             dfs(idx + 1, 0, cur_profit + prices[idx])
    #
    #     dfs(0, 0, 0)
    #     return self.ans

    def maxProfit(self, prices: List[int]) -> int:
        prices_len = len(prices)
        if prices_len < 2: return 0

        # dp[i][0]表示未持有, dp[i][1]表示持有
        dp = [[0, 0] for i in range(prices_len)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, prices_len):
            # 有或没有可保持不变, 可从有选择卖出
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # 有或没有可保持不变, 可从没有选择买入
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[prices_len - 1][0]


if __name__ == '__main__':
    # prices = [7, 1, 5, 3, 6, 4]
    prices = [7, 1, 5]
    ans = Solution().maxProfit(prices)
    print(ans)
