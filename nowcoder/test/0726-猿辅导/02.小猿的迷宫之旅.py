# -*- coding:utf-8 -*-
import sys

nmk = input().split()
nmk = [int(v) for v in nmk]
n, m, k = nmk[0], nmk[1], nmk[2]

matrix = []
for i in range(n):
    line = input().split()
    line = [int(v) for v in line]
    matrix.append(line)

memo = [[[0 for kk in range(12)] for j in range(502)] for i in range(502)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

import functools
@functools.lru_cache(None)
def solve(cur_x, cur_y, cur_k):
    # 记忆化节省计算
    if memo[cur_x][cur_y][cur_k]:
        return memo[cur_x][cur_y][cur_k]

    count = 1
    for i in range(4):
        new_x = cur_x + dx[i]
        new_y = cur_y + dy[i]
        if 0 <= new_x < n and 0 <= new_y < m:
            if matrix[new_x][new_y] > matrix[cur_x][cur_y]:
                count = max(count, solve(new_x, new_y, cur_k) + 1)
            else:
                if cur_k > 0:
                    count = max(count, solve(new_x, new_y, cur_k - 1) + 1)

    memo[cur_x][cur_y][cur_k] = count
    return count


max_value = 0
for i in range(n):
    for j in range(m):
        cur_value = solve(i, j, k)
        max_value = max(max_value, cur_value)
        # print(i, j, cur_value)
print(max_value)
