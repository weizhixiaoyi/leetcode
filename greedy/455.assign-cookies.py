# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g_len, s_len = len(g), len(s)
        if g_len == 0 or s_len == 0: return 0

        g = sorted(g)
        s = sorted(s)
        # print(g)
        # print(s)

        ans = 0
        i, j = 0, 0
        while i < g_len and j < s_len:
            if s[j] >= g[i]:
                i += 1
                j += 1
                ans += 1
            else:
                j += 1
        return ans


if __name__ == '__main__':
    g = [1, 2]
    s = [1, 2, 3]
    ans = Solution().findContentChildren(g, s)
    print(ans)
