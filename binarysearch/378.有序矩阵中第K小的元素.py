# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])

        import heapq
        val = []
        for i in range(m):
            for j in range(n):
                heapq.heappush(val, matrix[i][j])

        idx = 0
        while True:
            idx += 1
            cur = heapq.heappop(val)
            if k == idx:
                return cur
    """

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        left, right = matrix[0][0], matrix[m - 1][n - 1]
        # print(self.count(matrix, m, n, 13))
        while left < right:
            mid = (left + right) // 2
            cur_count = self.count(matrix, m, n, mid)
            # print(mid, cur_count)
            if cur_count >= k:
                right = mid
            else:
                left = mid + 1
        return left

    def count(self, matrix, m, n, val):
        cur_count = 0

        i, j = 0, n - 1
        while i < n and j >= 0:
            if val >= matrix[i][j]:
                cur_count += (j + 1)
                i += 1
            else:
                j -= 1
        return cur_count


if __name__ == '__main__':
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    ans = Solution().kthSmallest(matrix, k)
    print(ans)
