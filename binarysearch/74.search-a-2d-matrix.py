# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0: return False
        if len(matrix[0]) == 0: return False
        m, n = len(matrix), len(matrix[0])
        if matrix[0][0] > target or matrix[m - 1][n - 1] < target: return False

        def binary_search(line, target):
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if line[mid] == target:
                    return True
                if line[mid] < target:
                    left = mid + 1
                if line[mid] > target:
                    right = mid - 1
            return False

        if m == 1: return binary_search(matrix[0], target)
        # more than one line
        for i in range(0, m - 1):
            if target == matrix[i][0] or target == matrix[i + 1][0]:
                return True
            if matrix[i][0] < target and target < matrix[i + 1][0]:
                return binary_search(matrix[i], target)
        # last line
        return binary_search(matrix[m - 1], target)


if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 13
    ans = Solution().searchMatrix(matrix, target)
    print('F: ', ans)
