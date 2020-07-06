# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # dfs
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        # 硬币从大到小依次进行选择
        coins = sorted(coins, reverse=True)
        coins_len = len(coins)

        self.ans = float("inf")

        def helper(amount, coins, index, count):
            # 递归结束条件
            # 1. 已经满足
            if amount == 0:
                # print(count)
                self.ans = min(self.ans, count)
                return None
            # 2. 无法满足
            if index == coins_len:
                return None

            k = amount // coins[index]
            # 虽然(small k) + count会小于self.ans, 但k减小之后, 下次运算结果会大于目前ans, 所以还是可以直接忽略
            # k + count < self.ans是关键
            while k + count < self.ans and k >= 0:
                helper(amount - k * coins[index], coins, index + 1, count + k)
                k -= 1

        helper(amount, coins, 0, 0)
        return self.ans if self.ans != float("inf") else -1


if __name__ == '__main__':
    coins = [3, 7, 405, 436]
    amount = 8839
    ans = Solution().coinChange(coins, amount)
    print(ans)
