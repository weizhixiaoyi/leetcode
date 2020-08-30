# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums
        nums_len = len(nums)

        ans = []
        from collections import deque
        dq = deque()
        for i in range(k):
            while dq and dq[-1] < nums[i]:
                dq.pop()
            dq.append(nums[i])
        ans.append(dq[0])

        for i in range(k, nums_len):
            if dq[0] == nums[i - k]:
                dq.popleft()
            while dq and dq[-1] < nums[i]: dq.pop()
            dq.append(nums[i])
            ans.append(dq[0])
        return ans


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2
    ans = Solution().maxSlidingWindow(nums, k)
    print(ans)
