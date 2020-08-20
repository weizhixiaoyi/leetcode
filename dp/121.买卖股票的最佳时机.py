# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices_len = len(prices)
        if prices_len == 0 or prices_len == 1: return 0

        min_value = prices[0]
        # 定义dp状态, 假设第i天卖出股票的最大收益
        dp = [0 for i in range(prices_len)]
        for i in range(1, prices_len):
            min_value = min(min_value, prices[i])
            # 第i天选择不卖出股票, 选择卖出股票两种选择
            dp[i] = max(dp[i - 1], prices[i] - min_value)
        print(dp)
        return dp[prices_len - 1]


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    ans = Solution().maxProfit(prices)
    print(ans)
