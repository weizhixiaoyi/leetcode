# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        nums = M
        if not nums: return 0
        n = len(nums)

        def dfs(used, i):
            for j in range(0, n):
                if nums[i][j] == 1 and used[j] is False:
                    used[j] = True
                    dfs(used, j)

        used = [False for i in range(n)]
        ans = 0
        for i in range(n):
            if used[i] is False:
                dfs(used, i)
                ans += 1

        return ans


if __name__ == '__main__':
    M = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    # M = [[1, 1, 0],
    #      [1, 1, 1],
    #      [0, 1, 1]]
    ans = Solution().findCircleNum(M)
    print(ans)
