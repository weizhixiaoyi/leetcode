# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])

        def bfs(grid, k):
            start_x, start_y, end_x, end_y = 0, 0, m - 1, n - 1
            dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

            from queue import Queue
            q = Queue()
            q.put((start_x, start_y, k, 0))
            # 如果只有走和不走两种状态, 那么只需要利用used数组True or False进行记录即可.
            # 但此时1可进行走, 因此需记录(cur_x, cur_y, cur_k)是否出现在dict之中
            visted = {(0, 0, k)}
            grid[start_x][start_y] = 1
            min_value = float('inf')

            while not q.empty():
                cur = q.get()
                cur_x, cur_y, cur_k, cur_idx = cur[0], cur[1], cur[2], cur[3]
                if cur_x == end_x and cur_y == end_y and cur_k >= 0:
                    min_value = cur_idx
                    break

                for k in range(4):
                    new_x, new_y = cur_x + dx[k], cur_y + dy[k]
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n: continue

                    if grid[new_x][new_y] == 0 and (new_x, new_y, cur_k) not in visted:
                        q.put((new_x, new_y, cur_k, cur_idx + 1))
                        visted.add((new_x, new_y, cur_k))
                    elif grid[new_x][new_y] == 1 and cur_k > 0 and (new_x, new_y, cur_k - 1) not in visted:
                        q.put((new_x, new_y, cur_k - 1, cur_idx + 1))
                        visted.add((new_x, new_y, cur_k - 1))
            if min_value != float('inf'):
                return min_value
            else:
                return -1

        ans = bfs(grid, k)
        return ans


if __name__ == '__main__':
    # grid = [[0, 0, 0],
    #         [1, 1, 0],
    #         [0, 0, 0],
    #         [0, 1, 1],
    #         [0, 0, 0]]
    # k = 1
    # grid = [[0, 1, 1],
    #         [1, 1, 1],
    #         [1, 0, 0]]
    # k = 1
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
    k = 1
    ans = Solution().shortestPath(grid, k)
    print(ans)
