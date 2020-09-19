# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda d: (d[0], d[1]))
        intervals_len = len(intervals)
        # print(intervals)

        idx, ans = 0, []
        while idx < intervals_len:
            pre = intervals[idx]
            max_right = pre[1]
            while idx < intervals_len - 1 and max_right >= intervals[idx + 1][0]:
                max_right = max(max_right, intervals[idx + 1][1])
                idx += 1
            ans.append([pre[0], max_right])
            idx += 1
        return ans


if __name__ == '__main__':
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    ans = Solution().insert(intervals, newInterval)
    print(ans)
