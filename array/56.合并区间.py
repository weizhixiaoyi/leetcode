# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals = sorted(intervals, key=lambda d: (d[0], d[1]))
        intervals_len = len(intervals)

        idx = 0
        ans = []
        while idx < intervals_len:
            pre = intervals[idx]
            max_right = pre[1]
            while idx < intervals_len - 1 and max_right >= intervals[idx + 1][0]:
                max_right = max(max_right, intervals[idx + 1][1])
                idx += 1
            ans.append([pre[0], max_right])
            idx += 1
        # print(ans)
        return ans


if __name__ == '__main__':
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # intervals = [[1, 4], [4, 5]]
    # intervals = [[1, 4], [2, 3]]
    intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    ans = Solution().merge(intervals)
    print(ans)
