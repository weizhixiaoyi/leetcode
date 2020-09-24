# -*- coding:utf-8 -*-


def solve(n, m, nums):
    ans = 0
    for num in nums:
        ans += sum(num)
    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = []
    for i in range(n):
        line = list(map(int, input().split()))
        nums.append(line)
    ans = solve(n, m, nums)
    print(ans)
