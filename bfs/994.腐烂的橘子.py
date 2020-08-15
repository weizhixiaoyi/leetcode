# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])

        def bfs(cur_grid, start_x, start_y):
            dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
            from queue import Queue
            q = Queue()
            q.put((start_x, start_y, 0))
            cur_grid[start_x][start_y] = 0
            max_value = 0

            while not q.empty():
                cur = q.get()
                cur_x, cur_y, cur_step = cur[0], cur[1], cur[2]

                for k in range(4):
                    new_x, new_y = cur_x + dx[k], cur_y + dy[k]
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or cur_grid[new_x][new_y] == 0:
                        continue
                    if cur_grid[new_x][new_y] == 2:
                        max_value = cur_step + 1
                        q.queue.clear()
                        break
                    q.put((new_x, new_y, cur_step + 1))
                    cur_grid[new_x][new_y] = 0
            return max_value

        from copy import deepcopy
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur_step = bfs(deepcopy(grid), i, j)
                    if cur_step == 0: return -1
                    ans = max(ans, cur_step)
        return ans


if __name__ == '__main__':
    # grid = [[1, 2, 1, 1, 2, 1, 1]]
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    # grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    # grid = [[0, 2]]
    # grid = [[1, 2, 2]]
    ans = Solution().orangesRotting(grid)
    print(ans)
