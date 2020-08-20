# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    def maxProfit(self, prices: List[int]) -> int:
        prices_len = len(prices)
        if prices_len < 2: return 0

        dp = [[0 for j in range(prices_len)] for i in range(prices_len)]
        for i in range(0, prices_len - 1):
            min_value = prices[i]
            for j in range(i + 1, prices_len):
                min_value = min(min_value, prices[j])
                dp[i][j] = max(dp[i][j - 1], prices[j] - min_value)

        ans = dp[0][prices_len - 1]
        for j in range(1, prices_len - 1):
            ans = max(ans, dp[0][j] + dp[j + 1][prices_len - 1])
        # print(ans)
        return ans
    """

    def maxProfit(self, prices: List[int]) -> int:
        prices_len = len(prices)
        if prices_len < 2: return 0

        # 状态: dp[i]表示前i天, dp[i][0]或者dp[i][1]表示第i天是否买入或卖出
        K = 2
        dp = [[[0, 0] for j in range(K + 1)] for i in range(prices_len)]
        for i in range(0, prices_len):
            for k in range(1, K + 1):
                if i == 0:
                    dp[0][k][1] = -prices[i]
                    continue

                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        print(dp)
        return dp[prices_len - 1][K][0]


if __name__ == '__main__':
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    # prices = [1, 2, 3, 4, 5]
    ans = Solution().maxProfit(prices)
    print(ans)
