# -*- coding:utf-8 -*-

class Solution:
    # 直接进行计算会超时, 因此需要进行剪枝或者对答案进行缓存
    # 使用lru_cache将中国结果进行缓存, 不需要再每次进行计算, 减少计算次数.
    """
    import functools
    @functools.lru_cache(None)
    def tribonacci(self, n: int) -> int:
        # 递归截止条件
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # 递进和归并过程, 递归完成后返回答案
        ans = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return ans
    """

    # 将答案进行缓存
    """
    def tribonacci(self, n: int) -> int:
        def helper(k):
            if k == n + 1:
                return None
            dp[k] = dp[k - 1] + dp[k - 2] + dp[k - 3]
            helper(k + 1)

        dp = [0 for i in range(n + 1)]
        dp[1], dp[2] = 1, 1
        helper(3)
        return dp[n]
    """

    # 带剪枝的计算
    def tribonacci(self, n: int) -> int:
        def helper(k):
            if k == 0:
                return 0
            if dp[k] > 0:
                return dp[k]

            dp[k] = helper(k - 1) + helper(k - 2) + helper(k - 3)
            return dp[k]

        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1
        helper(n)
        return dp[n]


if __name__ == '__main__':
    n = 25
    ans = Solution().tribonacci(n)
    print(ans)
