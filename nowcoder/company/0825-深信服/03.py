# -*- coding:utf-8 -*-


def solve(nums, nums_len):
    maxB = 10001
    max_able = 0
    for i in range(1, maxB):
        cur_able = 0
        for k in range(nums_len):
            l, r = nums[k]
            if l <= i <= r:
                cur_able += 1
        max_able = max(max_able, cur_able)
    return max_able


def solve1(nums, nums_len, min_l, max_r):
    for i in range(0, nums_len):
        nums[i][0], nums[i][1] = nums[i][0] - min_l, nums[i][1] - min_l
    max_r -= min_l
    min_l = 0

    times = [0 for i in range(max_r + 1)]
    for i in range(0, nums_len):
        l, r = nums[i]
        for k in range(l, r + 1):
            times[k] += 1
    return max(times)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = []
        min_l = float('inf')
        max_r = float('-inf')
        for j in range(n):
            l, r = map(int, input().split())
            min_l = min(min_l, l)
            max_r = max(max_r, r)
            nums.append([l, r])
        # ans = solve(nums, n)
        ans = solve1(nums, n, min_l, max_r)
        print(ans)