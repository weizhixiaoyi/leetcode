# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0

        prices_len = len(prices)
        min_value = prices[0]
        max_ans = 0
        for i in range(1, prices_len):
            cur_ans = prices[i] - min_value
            if cur_ans > max_ans:
                max_ans = cur_ans
            if prices[i] < min_value:
                min_value = prices[i]
        return max_ans


if __name__ == '__main__':
    # prices = [7, 1, 5, 3, 6, 4]
    prices = [7, 6, 5, 4, 3, 2, 1]
    ans = Solution().maxProfit(prices)
    print(ans)
