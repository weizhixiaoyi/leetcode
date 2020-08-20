# -*- coding:utf-8 -*-

class Solution:
    """
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.ans = False
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        if s1_len + s2_len != s3_len: return False

        # 1. s1[i] == s3[k] or s2[j] == s3[k]时候再进行递归
        # 2. 带有记忆的递归
        memo = {}

        def dfs(i, j, k):
            if (i, j) in memo: return memo[(i, j)]
            if i == s1_len and j == s2_len and k == s3_len:
                memo[(i, j)] = True
                return True

            flag = False
            if i < s1_len and s1[i] == s3[k]:
                flag = dfs(i + 1, j, k + 1)
            if j < s2_len and s2[j] == s3[k]:
                flag = flag or dfs(i, j + 1, k + 1)
            memo[(i, j)] = flag
            return flag

        ans = dfs(0, 0, 0)
        return ans
    """

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        if s1_len + s2_len != s3_len: return False

        dp = [[False for j in range(s2_len + 1)] for i in range(s1_len + 1)]
        dp[0][0] = True


if __name__ == '__main__':
    # s1, s2, s3 = "aabcc", "dbbca", "aadbbcbcac"
    # s1, s2, s3 = "aabcc", "dbbca", "aadbbbaccc"
    # s1, s2, s3 = "cabbcaaacacbac", "acabaabacabcca", "cacabaabacaabccbabcaaacacbac"
    s1, s2, s3 = 'a', 'b', 'ab'
    ans = Solution().isInterleave(s1, s2, s3)
    print(ans)
