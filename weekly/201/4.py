# -*- coding:utf-8 -*-
from typing import List

"""
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        self.ans = 0
        cuts = sorted(cuts)

        def binary_search(l, r, nums):
            target = (l + r) // 2
            nums_len = len(nums)
            left, right = 0, nums_len - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left += 1
                if nums[mid] > target:
                    right -= 1
            return min(left, nums_len - 1)

        def helper(l, r, cuts):
            if l > r: return

            self.ans += (r - l)

            mid_index = binary_search(l, r, cuts)
            mid_value = cuts[mid_index]
            # print(mid_index, mid_value)
            # print('#' * 10)

            if mid_index <= len(cuts) and cuts[:mid_index] != []:
                helper(l, mid_value, cuts[: mid_index])
            if mid_index + 1 < len(cuts) and cuts[mid_index + 1:] != []:
                helper(mid_value, r, cuts[mid_index + 1:])

        helper(0, n, cuts)
        return self.ans
"""


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> float:
        cuts_sort = sorted(cuts)
        cuts_sort.insert(0, 0)
        cuts_sort.append(n)
        cuts_len = len(cuts_sort)

        dp = [[float('inf') for j in range(cuts_len)] for i in range(cuts_len)]
        for i in range(0, cuts_len - 1):
            dp[i][i] = 0
            dp[i][i + 1] = 0
        dp[cuts_len - 1][cuts_len - 1] = 0

        for i in range(cuts_len - 1, -1, -1):
            for j in range(i + 1, cuts_len):
                if j - i <= 1: continue
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + (cuts_sort[j] - cuts_sort[i]))
        return dp[0][-1]


if __name__ == '__main__':
    n = 7
    cuts = [1, 3, 4, 5]
    # n = 9
    # cuts = [5, 6, 1, 4, 2]
    # n = 10
    # cuts = [7, 8, 9, 2, 1]
    # n = 30
    # cuts = [18, 15, 13, 7, 5, 26, 25, 29]
    ans = Solution().minCost(n, cuts)
    print(ans)
