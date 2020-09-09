# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        from queue import Queue
        m, n = len(matrix), len(matrix[0])
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

        def bfs(start_x, start_y):
            q = Queue()
            q.put((start_x, start_y, 1))

            cur_ans = 0
            while not q.empty():
                cur = q.get()
                cur_x, cur_y, cur_level = cur
                cur_ans = max(cur_ans, cur_level)
                for k in range(4):
                    new_x, new_y = cur_x + dx[k], cur_y + dy[k]
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n: continue
                    if matrix[new_x][new_y] > matrix[cur_x][cur_y]:
                        if ans_list[new_x][new_y] != 0:
                            cur_ans = max(cur_ans, ans_list[new_x][new_y] + cur_level)
                        else:
                            q.put((new_x, new_y, cur_level + 1))
            return cur_ans

        max_ans, ans_list = 0, [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                cur_ans = bfs(i, j)
                ans_list[i][j] = cur_ans
                # print(ans_dict)
                # print(i, j, cur_ans)
                max_ans = max(max_ans, cur_ans)
        return max_ans


if __name__ == '__main__':
    # matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    matrix = [[7, 8, 9], [9, 7, 6], [7, 2, 3]]
    ans = Solution().longestIncreasingPath(matrix)
    print(ans)
