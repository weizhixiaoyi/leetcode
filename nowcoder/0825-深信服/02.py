# -*- coding:utf-8 -*-


def solve(nums_len, nums, l, r, k):
    cur_ans = 0
    for i in range(l - 1, r - 1):
        for j in range(i + 1, r):
            if nums[i] * nums[j] + nums[i] + nums[j] == k:
                cur_ans += 1
    return cur_ans


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums_len = n

    from collections import defaultdict

    nums_dict = defaultdict(list)
    for i in range(nums_len):
        nums_dict[nums[i]].append(i)

    for i in range(m):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
