# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        seq_len = len(seq)

        ans = [0 for i in range(seq_len)]
        depth = 0
        for i in range(seq_len):
            if seq[i] == '(':
                depth += 1
                ans[i] = depth % 2
            else:
                depth -= 1
                ans[i] = depth % 2
        return ans


if __name__ == '__main__':
    seq = "(()())"
    ans = Solution().maxDepthAfterSplit(seq)
    print(ans)
