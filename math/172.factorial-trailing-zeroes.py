# -*- coding:utf-8 -*-

import math


class Solution:
    # ans = n / 5 + n / 25 + n / 125 + ...
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += n // 5
            n = n // 5
        return ans



if __name__ == '__main__':
    n = 5
    ans = Solution().trailingZeroes(n)
    print('ans: ', ans)
