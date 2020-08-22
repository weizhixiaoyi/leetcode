# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(left, right, cur):
            if left == 0 and right == 0:
                ans.append(cur)
                return
            if left > right:
                return

            if left > 0:
                dfs(left - 1, right, cur + '(')
            if right > 0:
                dfs(left, right - 1, cur + ')')

        dfs(n, n, '')
        return ans


if __name__ == '__main__':
    n = 3
    ans = Solution().generateParenthesis(n)
    print(ans)
