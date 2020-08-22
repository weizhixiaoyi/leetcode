# -*- coding:utf-8 -*-

def solve(nums, n):
    m, n = n, n
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def dfs(cur_used, cur_x, cur_y, path, ans):
        if len(path) >= 5:
            # print(path)
            if path == 'CHINA':
                ans[0] += 1
            return

        for i in range(4):
            new_x, new_y = cur_x + dx[i], cur_y + dy[i]
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n or used[new_x][new_y]:
                continue
            used[new_x][new_y] = True
            dfs(cur_used, new_x, new_y, path + nums[new_x][new_y], ans)
            used[new_x][new_y] = False

    from copy import deepcopy
    used = [[False for j in range(n)] for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if nums[i][j] == 'C':
                cur_used = deepcopy(used)
                tmp = [0]
                cur_used[i][j] = True
                dfs(used, i, j, 'C', tmp)
                ans += tmp[0]
    return ans


if __name__ == '__main__':
    # n = 4
    # nums = [
    #     ['C', 'H', 'I', 'A'],
    #     ['C', 'A', 'N', 'T'],
    #     ['G', 'R', 'A', 'C'],
    #     ['B', 'B', 'D', 'E']
    # ]
    n = int(input())
    nums = []
    for i in range(n):
        line = input()
        nums.append(line)

    ans = solve(nums, n)
    print(ans)
