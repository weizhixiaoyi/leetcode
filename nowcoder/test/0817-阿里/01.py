# -*- coding:utf-8 -*-


def solve1(nn, kk, nums):
    all_sum = []
    for k in range(kk):
        cur_sum = []
        for i in range(nn - 1):
            for j in range(i + 1, nn):
                cur_sum.append(nums[i][k] + nums[j][k])
        all_sum.append(cur_sum)

    ans = 0
    sum_len = len(all_sum[0])
    for i in range(sum_len):
        flag = True
        for k in range(1, kk):
            if all_sum[k][i] != all_sum[k - 1][i]:
                flag = False
        if flag: ans += 1
    return ans


# x1 + y1 = x2 + y2 ==> x1 - x2 = - (y1 - y2)
def solve2(nn, kk, nums):
    from collections import defaultdict
    sum_dict = defaultdict(int)
    ans = 0
    for i in range(nn):
        line = nums[i]
        diff = [line[i] - line[i - 1] for i in range(1, kk)]
        diff_str = "#".join([str(v) for v in diff])
        if diff_str in sum_dict:
            ans += sum_dict[diff_str]

        diff_rev = [-v for v in diff]
        diff_rev_str = "#".join(str(v) for v in diff_rev)
        sum_dict[diff_rev_str] += 1
    print(ans)


if __name__ == '__main__':
    nk = list(map(int, input().split()))
    n, k = nk[0], nk[1]
    nums = []
    for i in range(n):
        line = list(map(int, input().split()))
        nums.append(line)
    ans1 = solve1(n, k, nums)
    print(ans1)

    ans2 = solve1(n, k, nums)
    print(ans2)
