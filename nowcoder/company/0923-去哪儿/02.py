# -*- coding:utf-8 -*-


class Solution:
    def solve(self, nums_len, nums_a, nums_b):
        dp = [[0 for j in range(nums_len + 1)] for i in range(nums_len + 1)]

        for i in range(nums_len):
            for j in range(nums_len):
                if nums_a[i] == nums_b[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        # print(dp)
        return dp[nums_len][nums_len]


if __name__ == '__main__':
    n = int(input())
    a = input().split()
    b = input().split()
    # n = 7
    # a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # b = ['b', 'd', 'a', 'c', 'f', 'g', 'e']
    ans = Solution().solve(n, a, b)
    print(ans)
