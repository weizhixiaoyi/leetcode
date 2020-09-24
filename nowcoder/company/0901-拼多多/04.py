# -*- coding:utf-8 -*-

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


def solve(n, nums, nums_len):
    if n < 100000:
        ans = 0
        for i in range(1, n + 1):
            for j in range(nums_len):
                if i % nums[j] == 0:
                    # print(i)
                    ans += 1
                    break
        return ans
    else:
        ans = 0
        for i in range(nums_len):
            ans += (n // nums[i])
        # print(ans)

        gcd_nums = []
        for i in range(nums_len):
            for j in range(nums_len):
                if i == j: continue
                value = (nums[i] * nums[j]) // gcd(nums[i], nums[j])
                gcd_nums.append(value)
        gcd_nums = list(set(gcd_nums))
        gcd_nums_len = len(gcd_nums)
        # print(gcd_nums)

        for i in range(gcd_nums_len):
            print(n // gcd_nums[i])
            ans -= (n // gcd_nums[i])
        return ans


"""
1000 3
2
3
5
"""

if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = []
    for i in range(m):
        cur = int(input())
        nums.append(cur)
    # n, m = 1000, 3
    # nums = [2, 3, 5]
    ans = solve(n, nums, m)
    print(ans)
