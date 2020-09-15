# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points: return []
        if not K: return []
        points_len = len(points)

        import heapq
        ans = []
        for i in range(points_len):
            cur_dis = points[i][0] ** 2 + points[i][1] ** 2
            if i < K:
                heapq.heappush(ans, (-cur_dis, points[i]))
            else:
                if cur_dis < -ans[0][0]:
                    heapq.heappop(ans)
                    heapq.heappush(ans, (-cur_dis, points[i]))
        # print(ans)
        ans = [v[1] for v in ans]
        return ans


if __name__ == '__main__':
    # points = [[3, 3], [5, -1], [-2, 4]]
    # K = 2
    points = [[1, 3], [-2, 2]]
    K = 1
    ans = Solution().kClosest(points, K)
    print(ans)
