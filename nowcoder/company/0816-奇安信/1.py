# -*- coding:utf-8 -*-


class Solution:
    def test(self, num_money):
        if num_money == 0: return 0
        dp = [0 for i in range(num_money + 1)]
        dp[1], dp[2], dp[3] = 1, 2, 4
        for i in range(4, num_money + 1):
            dp[i] = 1
            for j in range(1, i):
                dp[i] += dp[j]
        return dp[num_money]

    def CalulateMethodCount(self, num_money):

        if num_money == 0: return 0
        nums = [i + 1 for i in range(num_money)]

        self.ans = 0

        def dfs(nums, path):
            sum_path = sum(path)
            if sum_path >= num_money:
                if sum_path == num_money:
                    print(path)
                    self.ans += 1
                return

            for num in nums:
                path.append(num)
                dfs(nums, path)
                path.pop()

        dfs(nums, [])
        return self.ans


if __name__ == '__main__':
    # n = 5
    n = int(input())
    ans = Solution().CalulateMethodCount(n)
    t = Solution().test(n)
    print(ans)
    print(t)
