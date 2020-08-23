# -*- coding:utf-8 -*-


def solve(n, paths, paths_len, trans, trans_len):
    return n


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    nums = []
    for i in range(m):
        line = list(map(int, input().split()))
        nums.append(line)
    trans = []
    for i in range(k):
        line = list(map(int, input().split()))
        trans.append(line)
    ans = solve(n, nums, m, trans, k)
    print(ans)
