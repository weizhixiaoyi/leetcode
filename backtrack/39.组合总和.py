# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        from copy import deepcopy
        paths = []

        def helper(candidates, target, path):
            path_sum = sum(path)
            if path_sum >= target:
                if path_sum == target:
                    path_sort = sorted(path)
                    if path_sort not in paths: paths.append(deepcopy(path))
                return

            for num in candidates:
                path.append(num)
                helper(candidates, target, path)
                path.pop()

        helper(candidates, target, [])
        return paths


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    # candidates = [2, 3, 5]
    # target = 8
    ans = Solution().combinationSum(candidates, target)
    print(ans)
