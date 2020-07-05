# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s_len = len(s)
        s_last = dict()
        for i in range(0, s_len):
            s_last[s[i]] = i

        ans = []
        begin, end = 0, 0
        for i, c in enumerate(s):
            end = max(end, s_last[c])

            if i == end:
                ans.append(i - begin + 1)
                begin = i + 1
        return ans


if __name__ == '__main__':
    S = "aa"
    ans = Solution().partitionLabels(S)
    print(ans)
