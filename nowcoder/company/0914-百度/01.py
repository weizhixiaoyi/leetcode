# -*- coding:utf-8 -*-

class Solution:
    def solve(self, matrix, n):
        # print(matrix)
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        from queue import Queue

        def bfs(matrix, start_x, start_y):
            q = Queue()
            q.put((start_x, start_y))
            matrix[start_x][start_y] = '2'

            while not q.empty():
                cur_x, cur_y = q.get()
                for k in range(4):
                    new_x, new_y = cur_x + dx[k], cur_y + dy[k]
                    if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n: continue
                    if matrix[new_x][new_y] == '1' or matrix[new_x][new_y] == '2':
                        continue
                    matrix[new_x][new_y] = '2'
                    q.put((new_x, new_y))
            # print(matrix)

        for i in range(n):
            for j in range(n):
                if (i == 0 or i == n - 1 or j == 0 or j == n - 1) and matrix[i][j] == '0':
                    bfs(matrix, i, j)

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == '2':
                    matrix[i][j] = '0'
                    continue
                if matrix[i][j] == '0':
                    matrix[i][j] = '1'
        for i in range(n):
            print(''.join(matrix[i]))


if __name__ == '__main__':
    n = int(input())
    matrix = []
    for i in range(n):
        line = list(input())
        matrix.append(line)

    # n = 4
    # matrix = [
    #     [1, 1, 1, 1],
    #     [0, 1, 0, 1],
    #     [1, 1, 0, 1],
    #     [0, 0, 1, 0]
    # ]
    # matrix = [list(map(str, line)) for line in matrix]

    Solution().solve(matrix, n)
