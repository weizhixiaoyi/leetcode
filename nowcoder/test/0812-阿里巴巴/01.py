# -*- coding:utf-8 -*-

def solve(n, m):
    nums = [i + 1 for i in range(n)]

    from copy import deepcopy
    paths, path = [], []

    def dfs(start):
        if len(path) == m:
            paths.append(deepcopy(path))

        for k in range(start, n):
            path.append(nums[k])
            dfs(k + 1)
            path.pop()

    dfs(0)
    for p in paths:
        print(p)


if __name__ == '__main__':
    n, m = 10, 4
    ans = solve(n, m)
    print(ans)
