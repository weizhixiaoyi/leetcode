# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        if not land: return []
        m, n = len(land), len(land[0])
        dx = [-1, 0, 1, 0, -1, 1, 1, -1]
        dy = [0, 1, 0, -1, 1, 1, -1, -1]

        def dfs(cur_x, cur_y, cur_area):
            ans = 0
            for k in range(8):
                new_x, new_y = cur_x + dx[k], cur_y + dy[k]
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or land[new_x][new_y] != 0: continue
                land[new_x][new_y] = 1
                ans += (dfs(new_x, new_y, cur_area) + 1)
            return ans

        ans = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    cur_area = [0]
                    land[i][j] = 1
                    ans.append(dfs(i, j, cur_area) + 1)
        ans = sorted(ans)
        return ans


if __name__ == '__main__':
    land = [
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1]
    ]
    # land = [[0]]
    ans = Solution().pondSizes(land)
    print(ans)
