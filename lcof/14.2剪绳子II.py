# -*- coding:utf-8 -*-
# class Solution:
#     def cuttingRope(self, n: int) -> int:
#         self.nums = [0 for i in range(n + 1)]
#
#         from functools import lru_cache
#         @lru_cache(None)
#         def helper(n):
#             if n < 2:
#                 return 0
#             if n == 2:
#                 self.nums[n] = 1
#                 return 1
#
#             for i in range(1, n):
#                 self.nums[n] = max(self.nums[n], max(i * (n - i), i * helper(n - i)))
#
#             return self.nums[n]
#
#         ans = helper(n)
#         return ans


class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[2] = 1
        value = 1000000007

        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))

        return dp[n] % value


if __name__ == '__main__':
    n = 500
    ans = Solution().cuttingRope(n)
    print(ans)
