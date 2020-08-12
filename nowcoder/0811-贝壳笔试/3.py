# -*- coding:utf-8 -*-
from copy import deepcopy


def bfs(used, start_x, start_y, end_x, end_y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    from queue import Queue
    q = Queue()
    q.put((start_x, start_y, 0))
    used[start_x][start_y] = True
    flag = False
    ans = 0

    while not q.empty():
        cur = q.get()
        cur_x, cur_y, idx = cur[0], cur[1], cur[2]
        if cur_x == end_x and cur_y == end_y:
            flag = True
            ans = idx
            q.queue.clear()
        for k in range(4):
            new_x = cur_x + dx[k]
            new_y = cur_y + dy[k]
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m or used[new_x][new_y]:
                continue

            used[new_x][new_y] = True
            q.put((new_x, new_y, idx + 1))
    if flag:
        return ans
    else:
        return 0


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 求解所有路径用dfs,可以进行回溯, 同时也可以求解最优解
def dfs(used, cur_x, cur_y, end_x, end_y, idx, ans):
    if cur_x == end_x and cur_y == end_y:
        ans[0] = min(idx, ans[0])

    for k in range(4):
        new_x = cur_x + dx[k]
        new_y = cur_y + dy[k]
        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m or used[new_x][new_y]: continue
        used[new_x][new_y] = True
        dfs(used, new_x, new_y, end_x, end_y, idx + 1, ans)
        used[new_x][new_y] = False


if __name__ == '__main__':
    n, m = 3, 3
    matrix = [
        '...',
        '.#.',
        '...'
    ]
    used = [[False for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '#':
                used[i][j] = True

    idx = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '.':
                idx.append([i, j])
    idx_len = len(idx)

    # t = bfs(matrix, used, 0, 0, 2, 2)
    # ans = [float('inf')]
    # dfs(used, 0, 0, 0, 1, 0, ans)
    # print(ans[0])
    # print('#' * 10)

    ans = 0
    for i in range(idx_len - 1):
        for j in range(i + 1, idx_len):
            # cur = bfs(used, idx[i][0], idx[i][1], idx[j][0], idx[j][1])
            tmp = [float('inf')]
            dfs(deepcopy(used), idx[i][0], idx[i][1], idx[j][0], idx[j][1], 0, tmp)
            print(idx[i][0], idx[i][1], idx[j][0], idx[j][1], tmp[0])
    print(ans)
