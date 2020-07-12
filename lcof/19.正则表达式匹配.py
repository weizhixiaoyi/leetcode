# -*- coding:utf-8 -*-

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        if s_len == 0 and p_len == 0: return True
        if s_len !=0 and p_len == 0: return False

        dp = [[False for j in range(p_len + 1)] for i in range(s_len + 1)]
        dp[0][0] = True
        for i in range(0, s_len + 1):
            for j in range(0, p_len + 1):
                if j == 0:
                    continue
                if s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                if p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                if p[j - 1] == '*':
                    # 忽略
                    if j >= 2:
                        dp[i][j] = (dp[i][j] or dp[i][j - 2])
                    # 不忽略
                    if (i >= 1 and j >= 2 and s[i - 1] == p[j - 2]) or (i >= 1 and j >= 2 and p[j - 2] == '.'):
                        dp[i][j] = (dp[i][j] or dp[i - 1][j])

        # print(dp)
        return dp[s_len][p_len]


if __name__ == '__main__':
    s = "aab"
    b = "c*a*b"
    ans = Solution().isMatch(s, b)
    print(ans)
