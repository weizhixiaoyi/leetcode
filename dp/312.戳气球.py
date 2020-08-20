# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums_len = len(nums)

        used = [False for i in range(nums_len)]
        self.ans = 0

        def dfs(idx, used, max_value):
            if idx == 0:
                self.ans = max(self.ans, max_value)

            for i in range(0, nums_len):
                if used[i]: continue
                used[i] = True
                left, right = i - 1, i + 1
                while left >= 0 and used[left]:
                    left -= 1
                while right < nums_len and used[right]:
                    right += 1

                if left == -1 and right == nums_len:
                    cur_value = nums[i]
                elif left == -1:
                    cur_value = nums[i] * nums[right]
                elif right == nums_len:
                    cur_value = nums[i] * nums[left]
                else:
                    cur_value = nums[left] * nums[i] * nums[right]

                # print(idx, left, right, cur_value)

                dfs(idx - 1, used, max_value + cur_value)
                used[i] = False

        dfs(nums_len, used, 0)
        return self.ans


if __name__ == '__main__':
    nums = [3, 1, 5, 8]
    # nums = [35, 16, 83, 87, 84, 59, 48, 41, 20, 54]
    # nums = [1, 2, 3]
    ans = Solution().maxCoins(nums)
    print(ans)
