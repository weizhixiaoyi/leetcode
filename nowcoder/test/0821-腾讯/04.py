# -*- coding:utf-8 -*-

def solve1(sing, k):
    nums = []
    a, b, c, d = sing[0], sing[1], sing[2], sing[3]
    for i in range(b):
        nums.append(a)
    for j in range(d):
        nums.append(c)

    print(nums)

    def dfs(idx, used, path, target, ans):
        if sum(path) >= target:
            if sum(path) == target:
                print(idx, path)
                ans[0] += 1
            return

        for i in range(idx, len(nums)):
            if used[i]: continue
            used[i] = True
            path.append(nums[i])
            dfs(i + 1, used, path, target, ans)
            used[i] = False
            path.pop()

    ans = [0]
    used = [False for i in range(len(nums))]
    dfs(0, used, [], k, ans)
    return ans[0]


def solve(sing, k):
    nums = []
    a, b, c, d = sing[0], sing[1], sing[2], sing[3]
    for i in range(b):
        nums.append(a)
    for j in range(d):
        nums.append(c)
    nums = sorted(nums)
    amount = k
    nums_len = b + d
    value = 1000000007

    dp = [[0 for j in range(amount + 1)] for i in range(nums_len + 1)]
    dp[0][0] = 1
    for i in range(1, nums_len + 1):
        for j in range(0, amount + 1):
            dp[i][j] = dp[i - 1][j]
            if j - nums[i - 1] >= 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - nums[i - 1]]) % value
    # print(dp)
    return dp[nums_len][amount] % value


if __name__ == '__main__':
    k = 5
    sing = [2, 3, 3, 3]
    # k = 989
    # sing = [3, 17, 7, 39]
    # k = int(input())
    # sing = list(map(int, input().split()))
    ans = solve1(sing, k)
    print(ans)
