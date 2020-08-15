# -*- coding:utf-8 -*-


def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


def solve(nums, nums_len):
    nums = sorted(nums)
    flag = False
    for i in range(0, nums_len - 1):
        if gcd(nums[i], nums[i + 1]) == 1:
            flag = True
            break
    if flag:
        return 0
    else:
        return -1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        ans = solve(nums, n)
        print(ans)
