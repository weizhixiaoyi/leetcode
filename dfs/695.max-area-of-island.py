# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        px = [-1, 0, 1, 0]
        py = [0, 1, 0, -1]

        def helper(x, y, cur_grid):
            # 递归截止条件
            if (x < 0 or x >= m) or (y < 0 or y >= n) or grid[x][y] == 0:
                return 0

            # 说明此时grid[x][y] == 1, 所以可以继续走下去, 走之后需要置为0
            # 此处不需要另外的used矩阵来表示是否已经走过, 可直接通过grid上的0, 1来标记是否走过, 走过的标记为1
            if cur_grid[x][y]:
                cur_grid[x][y] = 0

                ans = 1
                for i in range(0, 4):
                    cur_x = x + px[i]
                    cur_y = y + py[i]
                    if (0 <= cur_x < m) and (0 <= cur_y < n) and grid[cur_x][cur_y]:
                        ans += helper(cur_x, cur_y, cur_grid)

                return ans

        ans = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j]:
                    # print(i, j)
                    ans = max(helper(i, j, grid), ans)
                    # print(ans)
                    # print('#' * 10)
        return ans


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    ans = Solution().maxAreaOfIsland(grid)
    print('ans: ', ans)
