# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A: return []
        A_len = len(A)

        from collections import Counter
        ans = Counter(A[0])
        for i in range(1, A_len):
            cur = Counter(A[i])
            # ans = ans & cur
            for key, value in ans.items():
                if key not in cur:
                    ans[key] = 0
                else:
                    ans[key] = min(ans[key], cur[key])
            ans = {key: value for key, value in ans.items() if value != 0}

        tmp = []
        for key, value in ans.items():
            tmp.extend([key] * value)
        return tmp


if __name__ == '__main__':
    A = ["bella", "label", "roller"]
    ans = Solution().commonChars(A)
    print(ans)
