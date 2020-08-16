# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # def maxDistance(self, position: List[int], m: int) -> int:
    #     position = sorted(position)
    #     position_len = len(position)
    #
    # if m == 2: return position[-1] - position[0]
    # m -= 2
    # used = [position[0], position[-1]]
    # position.pop(0), position.pop(-1)
    # not_used = position
    #
    # while m > 0:
    #     idx = -1
    #     max_value = 0
    #     for i in range(len(not_used)):
    #         cur_min_value = float('inf')
    #         for j in range(len(used)):
    #             cur_not_use = not_used[i]
    #             cur_use = used[j]
    #             cur_min_value = min(cur_min_value, abs(cur_not_use - cur_use))
    #         if cur_min_value > max_value:
    #             max_value = cur_min_value
    #             idx = i
    #     used.append(not_used[idx])
    #     not_used.pop(idx)
    #     m -= 1
    # used = sorted(used)
    #
    # print(used, not_used)
    # ans = float('inf')
    # for i in range(1, len(used)):
    #     ans = min(ans, used[i] - used[i - 1])
    # return ans

    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        position_len = len(position)
        if m == 2: return position[-1] - position[0]

        def ok(cur_len, m):
            m -= 1
            pre = position[0]
            for k in range(1, position_len):
                if position[k] - pre >= cur_len:
                    # print(m, pre, position[k])
                    m -= 1
                    pre = position[k]
                else:
                    continue

            # print(m)
            if m > 0:
                return -1
            else:
                return 1

        # print(position)
        # print(ok(3, m))
        # print()
        left, right = 0, position[-1]
        max_value = 0
        while left <= right:
            mid = (left + right) // 2
            flag = ok(mid, m)
            # print(mid, flag)
            if flag == 1:
                left = mid + 1
                max_value = max(max_value, mid)
            else:
                right = mid - 1
        return max_value


if __name__ == '__main__':
    # position = [1, 2, 3, 4, 7]
    # m = 3
    # position = [5, 4, 3, 2, 1, 1000000000]
    # m = 2
    # position = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # m = 4
    # position = [79, 74, 47, 22]
    # m = 4
    position = [94, 95, 37, 30, 67, 7, 5, 44, 26, 55, 42, 28, 97, 19, 100, 74, 13, 88, 18]
    m = 7
    ans = Solution().maxDistance(position, m)
    print(ans)
