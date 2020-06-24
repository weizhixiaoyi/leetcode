# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        if sum(piles) % 2 == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    piles = [5, 3, 4, 5]
    ans = Solution().stoneGame(piles)
    print('ans: ', ans)
