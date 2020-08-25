# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills: return False
        if bills[0] != 5: return False
        bills_len = len(bills)

        from collections import defaultdict
        counts = defaultdict(int)
        for i in range(bills_len):
            if bills[i] == 5:
                counts[5] += 1
                continue
            if bills[i] == 10:
                counts[10] += 1
                if counts[5]:
                    counts[5] -= 1
                    continue
                return False
            if bills[i] == 20:
                counts[20] += 1
                # 给10, 5
                if counts[10] and counts[5]:
                    counts[10] -= 1
                    counts[5] -= 1
                    continue
                # 给3张5
                if counts[5] >= 3:
                    counts[5] -= 3
                    continue
                return False
        return True


if __name__ == '__main__':
    # bills = [5, 5, 5, 10, 20]
    # bills = [10, 10]
    bills = [5, 5, 10, 10, 20]
    ans = Solution().lemonadeChange(bills)
    print(ans)
