# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        nums_len, topk, topk_len = len(nums), [], 0

        for i in range(nums_len):
            if topk_len < k:
                heapq.heappush(topk, nums[i])
                topk_len += 1
            else:
                if topk[0] < nums[i]:
                    heapq.heappop(topk)
                    heapq.heappush(topk, nums[i])

        return topk[0]


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    # nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    # k = 4
    ans = Solution().findKthLargest(nums, k)
    print(ans)
