# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        prices_len = len(prices)
        if prices_len < 2: return 0

        if k > prices_len // 2:
            dp = [[0, 0] for i in range(prices_len)]
            dp[0][1] = -prices[0]
            for i in range(1, prices_len):
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            return dp[prices_len - 1][0]

        dp = [[[0, 0] for j in range(k + 1)] for i in range(prices_len)]
        for i in range(0, prices_len):
            for j in range(1, k + 1):
                if i == 0:
                    dp[0][j][1] = -prices[i]
                    continue

                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        # print(dp)
        return dp[prices_len - 1][k][0]


if __name__ == '__main__':
    # prices = [3, 2, 6, 5, 0, 3]
    # k = 2
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    k = 2
    ans = Solution().maxProfit(k, prices)
    print(ans)
