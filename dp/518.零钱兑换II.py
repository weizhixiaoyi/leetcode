# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # def change(self, amount: int, coins: List[int]) -> int:
    #     coins = sorted(coins)
    #     n = len(coins)
    #     dp = [[0 for j in range(amount + 1)] for i in range(n + 1)]
    #     # 如果j - k * coins[i] == 0, 那么dp[i][j] = dp[i][j - k * coins[i]] = 1, 那么初始化时应该设dp[i][0] = 1
    #     for i in range(0, n + 1):
    #         dp[i][0] = 1
    #
    #     for i in range(1, n + 1):
    #         for j in range(1, amount + 1):
    #             if j - coins[i - 1] >= 0:
    #                 dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
    #             else:
    #                 dp[i][j] = dp[i - 1][j]
    #     # print(dp)
    #     return dp[n][amount]

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0 for i in range(amount + 1)]
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    dp[j] = dp[j] + dp[j - coins[i - 1]]

        # print(dp)
        return dp[amount]



if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    ans = Solution().change(amount, coins)
    print(ans)
