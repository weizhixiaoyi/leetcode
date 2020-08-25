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

    ans_dict = {}
    for i in range(0, nums_len - 1):
        cur_ans = 0
        for j in range(i + 1, nums_len):
            if nums[i] * nums[j] + nums[i] + nums[j] == k:
                cur_ans += 1
            ans_dict[(i, j)] = cur_ans
    # print(ans_dict)

    query = []
    for i in range(m):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        cur_ans = 0
        for i in range(l, r):
            cur_ans += ans_dict[(i, r)]
        print(cur_ans)
