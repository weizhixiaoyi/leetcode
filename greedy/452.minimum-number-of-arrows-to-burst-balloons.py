# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points_len = len(points)
        if points_len == 0: return 0
        if points_len == 1: return 1

        points = sorted(points, key=lambda d: d[1])
        # print(points)

        ans = 0
        pre = points[0]
        for i in range(1, points_len):
            cur = points[i]
            if pre[1] < cur[0]:
                ans += 1
            else:
                pre = cur
        return points_len - ans


if __name__ == '__main__':
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    # points = [[1, 2], [2, 3], [3, 4], [4, 5]]
    ans = Solution().findMinArrowShots(points)
    print('ans: ', ans)
