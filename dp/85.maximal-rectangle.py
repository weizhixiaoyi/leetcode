# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + 1
        max_value = 0
        for line in dp:
            cur_value = self.largest_rectange_in_histogram(line)
            # print(line)
            # print(cur_value)
            # print('#' * 10)
            max_value = max(cur_value, max_value)
        return max_value

    def largest_rectange_in_histogram(self, heights):
        if len(heights) == 0: return 0
        heights.insert(0, 0)
        heights.append(0)
        ist, max_rectange = [], 0
        for i in range(0, len(heights)):
            while (len(ist) != 0 and heights[i] < heights[ist[-1]]):
                cur_index = ist[-1]
                ist.pop()
                left = ist[-1] + 1
                right = i - 1
                max_rectange = max(max_rectange, (right - left + 1) * heights[cur_index])

            ist.append(i)

        return max_rectange


if __name__ == '__main__':
    matrix1 = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    matrix = [["0", "1"], ["0", "1"]]
    solution = Solution()
    ans = solution.maximalRectangle(matrix1)
    print('ans: ', ans)
