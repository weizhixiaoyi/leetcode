# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        for i in range(0, amount + 1):
            for j in range(n):
                if i - coins[j] < 0: continue
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        # print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    # coins = [1, 2, 5]
    # amount = 11
    coins = [2]
    amount = 3
    ans = Solution().coinChange(coins, amount)
    print(ans)
