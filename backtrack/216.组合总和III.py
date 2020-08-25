# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums, nums_len = [i + 1 for i in range(9)], 9

        def dfs(idx, path):
            if len(path) == k and sum(path) == n:
                ans.append(path)

            for i in range(idx, nums_len):
                dfs(i + 1, path + [nums[i]])

        ans = []
        dfs(0, [])
        return ans


if __name__ == '__main__':
    # k, n = 3, 7
    k, n = 3, 9
    ans = Solution().combinationSum3(k, n)
    print(ans)
