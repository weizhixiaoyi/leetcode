# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    def twoSum(self, n: int) -> List[float]:
        dp = [[0 for j in range(6 * n + 1)] for i in range(n + 1)]

        # 1个骰子初始化
        for j in range(7):
            dp[1][j] = 1

        for k in range(2, n + 1):
            for j in range(k, 6 * k + 1):
                for i in range(1, 7):
                    if j - i < 1:
                        break
                    dp[k][j] += dp[k - 1][j - i]

        ans = []
        all = pow(6, n)
        for j in range(n, 6 * n + 1):
            ans.append(dp[n][j] / all)
        return ans
    """

    def twoSum(self, n: int) -> List[float]:
        dp = [0 for i in range(6 * n + 1)]

        for j in range(1, 7):
            dp[j] = 1

        for k in range(2, n + 1):
            for j in range(6 * k, k - 1, -1):
                dp[j] = 0
                for i in range(0, 7):
                    if j - i < k - 1:
                        break
                    dp[j] += dp[j - i]

        # print(dp)
        ans = []
        all = pow(6, n)
        for j in range(n, 6 * n + 1):
            ans.append(dp[j] / all)
        return ans


if __name__ == '__main__':
    n = 3
    ans = Solution().twoSum(n)
    print(ans)
