# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        nums_len = len(nums)

        dp = [1 for i in range(nums_len)]
        count = [1 for i in range(nums_len)]

        for i in range(nums_len):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = max(dp[i], dp[j] + 1)
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        # print(dp)
        # print(count)
        max_value = max(dp)
        ans = 0
        for i in range(nums_len):
            if dp[i] == max_value:
                ans += count[i]
        return ans


if __name__ == '__main__':
    # nums = [1, 3, 5, 4, 7]
    nums = [1, 2, 4, 3, 5, 4, 7, 2]
    # nums = [1, 2, 4, 3, 5, 4]
    ans = Solution().findNumberOfLIS(nums)
    print(ans)
