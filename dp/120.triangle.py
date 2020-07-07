# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        triangle_len = len(triangle)
        if triangle_len == 0: return 0
        if triangle_len == 1: return triangle[0][0]

        dp = [[0 for j in range(len(triangle[i]))] for i in range(0, len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(1, triangle_len):
            triangle_i_len = len(triangle[i])
            for j in range(0, triangle_i_len):
                if j == 0:
                    dp[i][0] = dp[i - 1][0] + triangle[i][0]
                elif j == triangle_i_len - 1:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j] + triangle[i][j], dp[i - 1][j - 1] + triangle[i][j])

        return min(dp[-1])


if __name__ == '__main__':
    triangle = [
        [2],
        [3, 4],
        # [6, 5, 7],
        # [4, 1, 8, 3]
    ]
    ans = Solution().minimumTotal(triangle)
    print(ans)
