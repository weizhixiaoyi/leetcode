# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        def helper(s):
            if len(s) == 0: return []
            if len(s) == 1: return [s]

            list = helper(s[1:])
            ans = []
            for cur_str in list:
                ans.append(s[0] + cur_str)
                for k in range(1, len(cur_str)):
                    ans.append(cur_str[:k] + s[0] + cur_str[k:])
                ans.append(cur_str + s[0])
            return ans

        ans = helper(s)
        return list(set(ans))


if __name__ == '__main__':
    s = "abc"
    ans = Solution().permutation(s)
    print(ans)
