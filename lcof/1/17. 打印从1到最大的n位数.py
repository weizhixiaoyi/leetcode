# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [i + 1 for i in range(0, pow(10, n) - 1)]


if __name__ == '__main__':
    n = 2
    ans = Solution().printNumbers(n)
    print(ans)
