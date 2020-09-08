# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        stones_len = len(stones)

        while True:
            if stones_len >= 2:
                new_value = abs(stones[-1] - stones[-2])
                stones = stones[:-2] + [new_value]

            stones = sorted(stones)
            stones_len = len(stones)
            if stones_len == 1:
                return stones[0]
            if stones_len == 0:
                return 0


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    ans = Solution().lastStoneWeight(stones)
    print(ans)
