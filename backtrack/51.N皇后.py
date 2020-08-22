# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        nums = [['.' for j in range(n)] for i in range(n)]

        def valid(nums, row, col):
            # 检查列
            for k in range(0, row):
                if nums[k][col] == 'Q':
                    return False

            # 检查左上
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if nums[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # 检查右上
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if nums[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        from copy import deepcopy
        tmp = []

        def dfs(row, nums):
            if row == n:
                tmp.append(deepcopy(nums))

            for col in range(n):
                if not valid(nums, row, col):
                    continue

                nums[row][col] = 'Q'
                dfs(row + 1, nums)
                nums[row][col] = '.'

        dfs(0, nums)
        ans = []
        for t in tmp:
            cur = []
            for l in t:
                cur.append(''.join(l))
            ans.append(cur)
        return ans


if __name__ == '__main__':
    n = 4
    ans = Solution().solveNQueens(n)
    print(ans)
