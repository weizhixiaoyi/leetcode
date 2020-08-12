# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from copy import deepcopy
        candidates = sorted(candidates)
        candidates_len = len(candidates)
        ans = []

        def helper(start, path, cur_sum):
            if cur_sum >= target:
                if cur_sum == target:
                    ans.append(deepcopy(path))
                return

            for k in range(start, candidates_len):
                if k > start and candidates[k] == candidates[k - 1]: continue
                path.append(candidates[k])
                helper(k + 1, path, cur_sum + candidates[k])
                path.pop()

        helper(0, [], 0)
        return ans


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    ans = Solution().combinationSum2(candidates, target)
    print(ans)
