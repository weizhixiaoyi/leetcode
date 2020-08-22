# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n: return []
        nums = [i + 1 for i in range(n)]

        from copy import deepcopy
        ans = []

        def dfs(idx, path):
            if len(path) == k:
                ans.append(deepcopy(path))

            for i in range(idx, n):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        # print(ans)
        return ans


if __name__ == '__main__':
    n = 4
    k = 3
    ans = Solution().combine(n, k)
    print(ans)
