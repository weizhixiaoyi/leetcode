# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0: return 0
        if len(grid[0]) == 0: return 0
        m, n = len(grid), len(grid[0])

        from queue import Queue
        def helper(x, y, this_grid):
            # 移动方向
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]

            # 起始队列
            q = Queue()
            q.put((x, y))
            # 已经走过的位置标记为0
            this_grid[x][y] = 0
            this_ans = 1

            # 队列非空时继续寻找
            while not q.empty():
                cur = q.get()
                cur_x, cur_y = cur[0], cur[1]

                # 以当前队列位置进行左右扩散
                for k in range(0, 4):
                    new_x = cur_x + dx[k]
                    new_y = cur_y + dy[k]
                    # print(new_x, new_y)

                    if (0 <= new_x < m) and (0 <= new_y < n) and (this_grid[new_x][new_y] == 1):
                        q.put((new_x, new_y))
                        # print(new_x, new_y)
                        this_grid[new_x][new_y] = 0
                        this_ans += 1
            return this_ans

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
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
