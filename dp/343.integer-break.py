# -*- coding:utf-8 -*-

class Solution:
    # 递归实现: 超时
    # def integerBreak(self, n: int) -> int:
    #     values = [i + 1 for i in range(n - 1)]
    #     values = sorted(values, reverse=True)
    #
    #     # 从values中取出找到能够组成n个个数
    #     from copy import deepcopy
    #     self.ans = 0
    #     self.path = []
    #
    #     from functools import lru_cache
    #     from functools import reduce
    #     # @functools.lru_cache(None)
    #     def helper(n, values, index):
    #         if n == 0:
    #             return True
    #
    #         if n < 0 or index == len(values):
    #             return False
    #
    #         # for value in values:
    #         #     self.path.append(value)
    #         #     if helper(n - value, values):
    #         #         print(self.path)
    #         #         mul = reduce(lambda x, y: x * y, self.path)
    #         #         self.ans = max(self.ans, mul)
    #         #
    #         #     self.path.pop()
    #
    #         k = n // values[index]
    #         while k >= 0:
    #             if k > 0:
    #                 self.path.append(values[index])
    #             if helper(n - k * values[index], values, index + 1):
    #                 print(self.path)
    #                 self.ans = max(self.ans, reduce(lambda x,y: x * y, self.path))
    #             if k > 0:
    #                 self.path.pop()
    #             k -= 1
    #
    #         return False
    #
    #     helper(n, values, 0)
    #     return self.ans

    # 寻找状态转移方法 dp[n] = max(i * ( n - i), i * dp[n - i))
    # def integerBreak(self, n: int) -> int:
    #     self.memory = [0 for i in range(59)]
    #
    #     def helper(n):
    #         if n == 2:
    #             return 1
    #         # if n == 1:
    #         #     return 1
    #
    #         if self.memory[n] != 0:
    #             return self.memory[n]
    #
    #         res = -1
    #         for i in range(1, n):
    #             res = max(res, max(i * (n - i), i * helper(n - i)))
    #
    #         self.memory[n] = res
    #         return res
    #
    #     ans = helper(n)
    #     return ans

    def integerBreak(self, n: int):
        dp = [0 for i in range(59)]
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))

        return dp[n]


if __name__ == '__main__':
    n = 10
    ans = Solution().integerBreak(n)
    print(ans)
