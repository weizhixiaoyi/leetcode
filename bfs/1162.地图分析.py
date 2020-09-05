# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])

        flag1, flag2 = False, False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    flag1 = True
                if grid[i][j] == 0:
                    flag2 = True
        if not flag1 or not flag2:
            return -1

        def bfs(start_x, start_y, used):
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]

            from queue import Queue
            q = Queue()
            q.put((start_x, start_y))
            used[start_x][start_y] = True

            while not q.empty():
                cur_size = q.qsize()
                while cur_size:
                    cur_x, cur_y = q.get()
                    for k in range(4):
                        new_x, new_y = cur_x + dx[k], cur_y + dy[k]
                        if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or used[new_x][new_y]: continue
                        if grid[new_x][new_y] == 0:
                            q.put((new_x, new_y))
                            used[new_x][new_y] = True
                        if grid[new_x][new_y] == 1:
                            return abs(new_x - start_x) + abs(new_y - start_y)
                    cur_size -= 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    used = [[False for j in range(n)] for i in range(m)]
                    ans = max(ans, bfs(i, j, used))
        return ans
    """

    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])

        from queue import Queue
        q = Queue()
        flag1, flag2 = False, False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    flag1 = True
                    q.put((i, j))
                if grid[i][j] == 0:
                    flag2 = True
        if not flag1 or not flag2:
            return -1

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        path_len = 0
        while not q.empty():
            q_size = q.qsize()
            path_len += 1
            while q_size:
                cur_x, cur_y = q.get()
                for k in range(4):
                    new_x, new_y = cur_x + dx[k], cur_y + dy[k]
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or grid[new_x][new_y] != 0: continue
                    grid[new_x][new_y] = path_len
                    q.put((new_x, new_y))

                q_size -= 1
        # print(grid)
        ans = max(map(max, grid))
        return ans


if __name__ == '__main__':
    # grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    ans = Solution().maxDistance(grid)
    print(ans)
