# -*- coding:utf-8 -*-
from copy import deepcopy


def pan1(cur, nums):
    for num in nums:
        s, m, n = num
        common = 0
        for c in s:
            if c in cur:
                common += 1
        if common != m + n:
            return False
    return True


def pan2(cur, nums, real_len):
    for num in nums:
        s, m, n = num
        right1 = 0
        used = [0 for i in range(real_len)]
        for i in range(real_len):
            if s[i] == cur[i]:
                right1 += 1
                used[i] = 1
        if right1 != m:
            return False

        remove_str = []
        for i in range(real_len):
            if used[i] == 0:
                remove_str.append(cur[i])
        right2 = 0
        for i in range(real_len):
            if s[i] in remove_str:
                right2 += 1
        if right2 != n:
            return False

    return True


def solve(real_len, nums):
    all_char = []
    for num in nums:
        s = num[0]
        for c in s:
            if c not in all_char:
                all_char.append(c)
    all_char = sorted(all_char)
    all_char_len = len(all_char)
    print(all_char)

    # 利用子集找出存在的元素
    def dfs1(idx, path, flag):
        if flag[0] is True:
            return
        if len(path) >= real_len:
            cur_candidate = ''.join(path)
            if len(cur_candidate) == real_len and pan1(cur_candidate, nums):
                candidate.append(deepcopy(cur_candidate))
                flag[0] = True
            return

        for i in range(idx, all_char_len):
            path.append(all_char[i])
            dfs1(i + 1, path, flag)
            path.pop()

    candidate = []
    dfs1(0, [], [False])
    candidate = list(candidate[0])
    print(candidate)

    # 利用排列找出正确顺序
    def dfs2(path, ans, flag):
        if flag[0] is True:
            return
        if len(path) == real_len:
            cur_path = ''.join(path)
            if pan2(cur_path, nums, real_len):
                ans.append(deepcopy(cur_path))
                flag[0] = True

        for c in candidate:
            if c in path: continue
            path.append(c)
            dfs2(path, ans, flag)
            path.pop()

    ans = []
    dfs2([], ans, [False])
    return ans[0]


if __name__ == '__main__':
    p = int(input())
    t = int(input())
    nums = []
    for i in range(t):
        line = input().split()
        s, m, n = line[0], int(line[1]), int(line[2])
        nums.append([s, m, n])
    ans = solve(p, nums)
    print(ans)