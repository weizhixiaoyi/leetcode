# -*- coding:utf-8 -*-

class Solution:
    def cuttingRope(self, n: int) -> int:
        self.nums = [0 for i in range(n + 1)]

        from functools import lru_cache
        @lru_cache(None)
        def helper(n):
            if n < 2:
                return 0
            if n == 2:
                self.nums[n] = 1
                return 1

            for i in range(1, n):
                self.nums[n] = max(self.nums[n], max(i * (n - i), i * helper(n - i)))

            return self.nums[n]

        ans = helper(n)
        return ans


if __name__ == '__main__':
    n = 2
    ans = Solution().cuttingRope(n)
    print(ans)
