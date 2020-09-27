# -*- coding:utf-8 -*-


class Solution:
    def solve(self, n, m, matrix):
        m, n = n, m

        from queue import Queue
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

        def bfs(start_x, start_y, cur_matrix):
            q = Queue()
            q.put((start_x, start_y, 0))
            cur_matrix[start_x][start_y] = '1'

            while not q.empty():
                cur_x, cur_y, cur_level = q.get()

                for k in range(4):
                    new_x, new_y, = cur_x + dx[k], cur_y + dy[k]
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n: continue
                    if cur_matrix[new_x][new_y] == '1' or cur_matrix[new_x][new_y] == 'X': continue
                    if cur_matrix[new_x][new_y] == 'T':
                        return cur_level + 1
                    q.put((new_x, new_y, cur_level + 1))
                    cur_matrix[new_x][new_y] = '1'
            return float('inf')

        from copy import deepcopy
        min_value = float('inf')
        ans_point = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'X':
                    cur_matrix = deepcopy(matrix)
                    cur_ans = bfs(i, j, cur_matrix)
                    if cur_ans < min_value:
                        min_value = cur_ans
                    ans_point.append((cur_ans, i, j))
        if min_value == float('inf'):
            print(0)
        else:
            print(min_value)
            for i in range(len(ans_point)):
                cur_ans, cur_x, cur_y = ans_point[i]
                if cur_ans == min_value:
                    print(cur_x, cur_y, end=' ')
            print()


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        line = list(input())
        matrix.append(line)
    # print(n, m, matrix)

    Solution().solve(n, m, matrix)
