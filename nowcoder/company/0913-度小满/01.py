# -*- coding:utf-8 -*-

class Solution:
    def solve(self, n, k, matrix):
        if n > 20:
            return "No solution"
        else:
            start_x, start_y, end_x, end_y = 0, 0, n - 1, n - 1
            dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

            self.k = k
            self.ans = float('inf')

            def dfs(cur_x, cur_y, matrix, cur_time):
                if cur_x == end_x and cur_y == end_y:
                    self.ans = min(self.ans, cur_time)

                for k in range(4):
                    new_x, new_y = cur_x + dx[k], cur_y + dy[k]
                    if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n or matrix[new_x][new_y] == '1': continue
                    if cur_time > self.ans: continue
                    # print(new_x, new_y)
                    tmp = matrix[new_x][new_y]
                    tmp_time = cur_time
                    matrix[new_x][new_y] = '1'
                    add_time = 0
                    if tmp == '0':
                        add_time = 1
                    elif tmp == '#':
                        add_time = self.k + 1
                    dfs(new_x, new_y, matrix, cur_time + add_time)
                    matrix[new_x][new_y] = tmp
                    cur_time = tmp_time

            matrix[0][0] = '1'
            dfs(0, 0, matrix, 0)
            if self.ans != float('inf'):
                return self.ans
            else:
                return "No solution"


if __name__ == '__main__':
    n, k = map(int, input().split())
    matrix = []
    for i in range(n):
        line = list(input())
        matrix.append(line)
    # n, k = 3, 2
    # matrix = [
    #     ['0', '#', '0'],
    #     ['0', '#', '1'],
    #     ['0', '0', '0']
    # ]
    ans = Solution().solve(n, k, matrix)
    print(ans)
