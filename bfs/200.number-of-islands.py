# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0: return 0
        if len(grid[0]) == 0: return 0
        m, n = len(grid), len(grid[0])
        self.grid = grid

        from queue import Queue
        def helper(x, y):
            # 定义移动方向
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]

            # 初始化位置并将走过的位置标记为0
            q = Queue()
            q.put((x, y))
            self.grid[x][y] = "0"

            # 根据定义的方向进行搜索
            while not q.empty():
                cur = q.get()
                cur_x, cur_y = cur[0], cur[1]

                for k in range(0, 4):
                    new_x = cur_x + dx[k]
                    new_y = cur_y + dy[k]

                    if (0 <= new_x < m) and (0 <= new_y < n) and (self.grid[new_x][new_y] == "1"):
                        q.put((new_x, new_y))
                        self.grid[new_x][new_y] = "0"

        ans = 0
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == "1":
                    helper(i, j)
                    ans += 1
        return ans


if __name__ == '__main__':
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    ans = Solution().numIslands(grid)
    print('ans: ', ans)
