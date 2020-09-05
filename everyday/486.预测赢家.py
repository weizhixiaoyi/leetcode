# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        def dfs(left, right, nums, a_score, b_score, is_a):
            if left > right:
                # print(a_score, b_score)
                return a_score >= b_score

            if is_a:
                # 轮到A选, 只要有一种可能A成功即可; 所以采用or
                return dfs(left + 1, right, nums, a_score + nums[left], b_score, False) or dfs(left, right - 1, nums, a_score + nums[right], b_score, False)
            else:
                # 轮到B选, 只有B绝对输的情况下, A才能赢; 所以采用and
                return dfs(left + 1, right, nums, a_score, b_score + nums[left], True) and dfs(left, right - 1, nums, a_score, b_score + nums[right], True)

        ans = dfs(0, nums_len - 1, nums, 0, 0, True)
        return ans


if __name__ == '__main__':
    nums = [1, 5, 2]
    ans = Solution().PredictTheWinner(nums)
    print(ans)
