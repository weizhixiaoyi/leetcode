# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        A_len, B_len = len(A), len(B)
        if (A_len == 0) or (B_len == 0): return 0

        dp = [[0 for j in range(B_len + 1)] for i in range(A_len + 1)]
        ans = 0
        for i in range(A_len):
            for j in range(B_len):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = 0
                ans = max(ans, dp[i + 1][j + 1])
        return ans


if __name__ == '__main__':
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    ans = Solution().findLength(A, B)
    print(ans)
