# -*- coding:utf-8 -*-

m, n = 5, 5
matrix = [
    ['0', '2', '1', '1', '1'],
    ['0', '1', 'a', '0', 'A'],
    ['0', '1', '0', '0', '3'],
    ['0', '1', '0', '0', '1'],
    ['0', '1', '1', '1', '1']
]


def bfs(start_i, start_j):
    pass


ans = True
for i in range(m):
    for j in range(n):
        if matrix[i][j] == '2':
            ans = bfs(i, j)
            break
print(ans)
