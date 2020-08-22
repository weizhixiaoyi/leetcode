# -*- coding:utf-8 -*-

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        self.memo = {}

        def dfs(K, N):
            if N == 0: return 0
            if K == 1: return N
            if (K, N) in self.memo:
                return self.memo[(K, N)]

            res = float('inf')
            for i in range(1, N + 1):
                res = min(res, max(dfs(K, N - i), dfs(K - 1, i - 1)) + 1)
            self.memo[(K, N)] = res
            return res

        ans = dfs(K, N)
        return ans


if __name__ == '__main__':
    K, N = 2, 6
    ans = Solution().superEggDrop(K, N)
    print(ans)
