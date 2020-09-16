# -*- coding:utf-8 -*-


"""
class Solution:
    def solve(self, nums, target):
        nums = sorted(nums, reverse=True)
        self.ans = float('inf')

        def dfs(nums, path, cur_target):
            if cur_target < 0:
                return
            if cur_target == 0:
                # print(path)
                self.ans = min(self.ans, len(path))

            for num in nums:
                if cur_target < num: continue
                path.append(num)
                cur_target -= num
                dfs(nums, path, cur_target)
                path.pop()
                cur_target += num

        dfs(nums, [], target)
        return self.ans
"""


class Solution:
    def solve(self, nums, target):
        nums_len = len(nums)
        nums = sorted(nums)

        # dp[target]表示target需要多少
        # 初始化
        dp = [float('inf') for i in range(target + 1)]
        for i in range(nums_len):
            dp[nums[i]] = 1
        # print(dp)

        for i in range(nums_len):
            for j in range(0, target + 1):
                if j >= nums[i]:
                    dp[j] = min(dp[j], dp[j - nums[i]] + 1)
        # print(dp)
        return dp[target]


if __name__ == '__main__':
    nums = [1, 2, 5]
    target = 9
    # nums = [1, 2]
    # target = 3

    ans = Solution().solve(nums, target)
    print(ans)
