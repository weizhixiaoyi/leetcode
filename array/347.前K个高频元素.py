# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1

        # way1
        # nums_dict = sorted(nums_dict.items(), key=lambda d: d[1], reverse=True)
        # ans, idx = [], 0
        # for key, value in nums_dict:
        #     idx += 1
        #     ans.append(key)
        #     if idx >= k: break

        # way2
        print(nums_dict)
        import heapq
        topk, topk_len = [], 0
        for key, value in nums_dict.items():
            if topk_len < k:
                heapq.heappush(topk, (value, key))
                topk_len += 1
            else:
                if topk[0][0] < value:
                    heapq.heappop(topk)
                    heapq.heappush(topk, (value, key))
        # print(topk)
        ans = [v2 for v1, v2 in topk]
        return ans


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    ans = Solution().topKFrequent(nums, k)
    print(ans)
