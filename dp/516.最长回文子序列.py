# -*- coding:utf-8 -*-

import pprint


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_len = len(s)
        dp = [[-1 for j in range(s_len)] for i in range(s_len)]
        for i in range(0, s_len):
            for j in range(0, s_len):
                # i到i的长度为1, 应设dp状态为1
                if i == j: dp[i][i] = 1
                # i > j时候不存在子序列, 设置为0
                if i > j: dp[i][j] = 0
        for i in range(s_len - 2, -1, -1):
            for j in range(i + 1, s_len, 1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        # print(dp)
        return dp[0][s_len - 1]


if __name__ == '__main__':
    s = "cbbd"
    ans = Solution().longestPalindromeSubseq(s)
    print(ans)
