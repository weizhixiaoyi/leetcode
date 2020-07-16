# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # O(nlogn)
    # def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
    #     arr_sort = sorted(arr)
    #     return arr_sort[:k]

    # heapq O(nlogk)
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        import heapq
        topk = [-x for x in arr[:k]]
        heapq.heapify(topk)
        print(topk)

        for i in range(k, len(arr)):
            print(-topk[0])
            if -topk[0] > arr[i]:
                heapq.heappop(topk)
                heapq.heappush(topk, -arr[i])
        topk = [-x for x in topk]
        return topk

    # O(nklogk)
    # def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
    #     arr_len = len(arr)
    #     if arr_len == 0: return []
    #     if k == 0: return []
    #
    #     mink = []
    #     mink_len = 0
    #     for a in arr:
    #         if mink_len < k:
    #             mink.append(a)
    #             mink_len += 1
    #             continue
    #         mink = sorted(mink)
    #         if mink[-1] > a:
    #             mink.pop()
    #             mink.append(a)
    #     return mink


if __name__ == '__main__':
    arr = [0, 1, 2, 1]
    k = 2
    ans = Solution().getLeastNumbers(arr, k)
    print(ans)
