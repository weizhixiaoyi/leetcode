# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if (not nums) or (k == 0): return []
        nums_len = len(nums)

        ans = []
        from collections import deque
        dq = deque()
        # 未填满
        for i in range(0, k):
            while dq and nums[i] > dq[-1]: dq.pop()
            dq.append(nums[i])
        ans.append(dq[0])
        # print(dq)

        # 滑动窗口
        for i in range(k, nums_len):
            if dq[0] == nums[i - k]: dq.popleft()
            while dq and nums[i] > dq[-1]: dq.pop()
            dq.append(nums[i])
            ans.append(dq[0])
            # print(dq)
        return ans


if __name__ == '__main__':
    nums = [1, 3, -1, 7, 5, 3, 6, 7]
    k = 3
    ans = Solution().maxSlidingWindow(nums, k)
    print(ans)
