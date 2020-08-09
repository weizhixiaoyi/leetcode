# -*- coding:utf-8 -*-

def solve(n, nums):
    ans = 0
    nums = sorted(nums)
    for num in nums:
        if num == 1:
            continue
        elif num == 2:
            ans += 1
        elif num == 3:
            ans += 1
        else:
            if num % 2 == 0:
                ans += (num // 2)
            else:
                ans += 1
                num -= 3
                ans += (num // 2)
    return ans


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    # n = 3
    # nums = [5, 3, 7]
    ans = solve(n, nums)
    print(ans)
