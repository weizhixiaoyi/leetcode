# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def binary_search(line, k=-1):
            left, right = 0, len(line) - 1
            while left <= right:
                mid = left + (right - left) // 2
                # if line[mid] == k:
                #     return mid
                if line[mid] <= k:
                    right = mid - 1
                if line[mid] > k:
                    left = mid + 1
            return left

        ans = 0
        for line in grid:
            idx = binary_search(line)
            ans += len(line) - idx
        # print(ans)
        return ans


if __name__ == '__main__':
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    ans = Solution().countNegatives(grid)
    print('ans: ', ans)
