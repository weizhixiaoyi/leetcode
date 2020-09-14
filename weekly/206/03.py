# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points_len = len(points)
        if points_len == 1: return 0
        points = sorted(points, key=lambda d: (d[0], d[1]))
        # print(points)

        for k in range(points_len):
            ans = 0
            points = points[k:] + points[:k]
            print(points)

            con = set()
            for i in range(points_len - 1):
                min_value = float('inf')
                min_idx = -1
                for j in range(points_len):
                    if i == j: continue
                    if (i, j) in con or (j, i) in con: continue

                    p1, p2 = points[i], points[j]
                    cur_value = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                    if cur_value < min_value:
                        min_value = cur_value
                        min_idx = j
                ans += min_value
                # print(i, min_idx, min_value)
                con.add((i, min_idx))
            print(con)
            print(ans)
        return ans


if __name__ == '__main__':
    # points = [[-14, -14], [-18, 5], [18, -10], [18, 18], [10, -2]]
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    # points = [[3, 12], [-2, 5], [-4, 1]]
    # points = [[-1000000, -1000000], [1000000, 1000000]]
    # points = [[0,0],[1,1],[1,0],[-1,1]]
    ans = Solution().minCostConnectPoints(points)
    print(ans)
