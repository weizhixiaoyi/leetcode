# -*- coding:utf-8 -*-


def sovle(n):
    dp = [0 for i in range(100 + 1)]

    def fib(n):
        if n == 1:
            dp[1] = 1
            return 1
        if n == 0:
            dp[0] = 1
            return 1
        if dp[n]:
            return dp[n]
        dp[n] = fib(n - 1) + fib(n - 2)
        return dp[n]

    tmp = fib(100)
    ans = [[0 for j in range(n)] for i in range(n)]
    nums = dp[:n * n]
    left, right, top, bottom = 0, n - 1, 0, n - 1
    while nums:
        # left to right
        for k in range(left, right + 1):
            ans[top][k] = nums.pop()
        top += 1
        if top > bottom: break

        # top to bottom
        for k in range(top, bottom + 1):
            ans[k][right] = nums.pop()
        right -= 1
        if left > right: break

        # right to left
        for k in range(right, left - 1, - 1):
            ans[bottom][k] = nums.pop()
        bottom -= 1
        if top > bottom: break

        # bottom to top
        for k in range(bottom, top - 1, -1):
            ans[k][left] = nums.pop()
        left += 1
        if left > right: break

    for line in ans:
        tmp = [str(v) for v in line]
        tmp = ' '.join(tmp)
        print(tmp)


if __name__ == '__main__':
    # n = 3
    n = int(input())
    sovle(n)
