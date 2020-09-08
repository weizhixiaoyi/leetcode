# -*- coding:utf-8 -*-

def solve1(n, m, grid):
    # print(grid)
    visit = [0 for i in range(n + 1)]
    dis = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        dis[i] = grid[1][i]

    dis[1] = 0
    visit[1] = 1
    pos = 1
    for i in range(1, n + 1):
        min_value = float('inf')
        for j in range(1, n + 1):
            if (visit[j] == 0 and min_value > dis[j]):
                min_value = dis[j]
                pos = j
        visit[pos] = 1
        for j in range(1, n + 1):
            if visit[j] == 0 and dis[j] > dis[pos] + grid[pos][j]:
                dis[j] = dis[pos] + grid[pos][j]

    return dis[n]


def solve2(n, m, grid):
    # print(grid)
    visit = [0 for i in range(n + 1)]
    dis = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        dis[i] = grid[n][i]

    dis[n] = 0
    visit[n] = 1
    pos = n
    for i in range(n, 0, -1):
        min_value = float('inf')
        for j in range(n, 0, -1):
            if visit[j] == 0 and min_value > dis[j]:
                min_value = dis[j]
                pos = j
        visit[pos] = 1
        for j in range(n, 0, -1):
            if visit[j] == 0 and dis[j] > dis[pos] + grid[pos][j]:
                dis[j] = dis[pos] + grid[pos][j]
    return dis[1]


if __name__ == '__main__':
    n, m, t = list(map(int, input().split()))
    grid = [[float('inf') for j in range(n + 1)] for i in range(n + 1)]
    for i in range(m):
        s, e, d = list(map(int, input().split()))
        grid[s][e] = d
    ans = t * (solve1(n, m, grid) + solve2(n, m, grid))
    print(ans)
