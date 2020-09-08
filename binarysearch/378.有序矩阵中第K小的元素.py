# -*- coding:utf-8 -*-
from typing import List


class Solution:
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


if __name__ == '__main__':
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 9
    ans = Solution().kthSmallest(matrix, k)
    print(ans)
