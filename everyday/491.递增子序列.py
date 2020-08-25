# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        used = [False for i in range(nums_len)]
        ans = []

        from copy import deepcopy
        def dfs(idx, path):
            path_len = len(path)
            print(path)
            if path_len >= 2:
                tmp = deepcopy(path)
                tmp_sort = sorted(tmp)

                if tmp_sort == tmp and path not in ans:
                    ans.append(deepcopy(path))

            for i in range(idx, nums_len):
                # print(i, i - 1, nums[i], nums[i - 1])
                # if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue

                used[i] = True
                path.append(nums[i])
                dfs(i + 1, path)
                used[i] = False
                path.pop()

        dfs(0, [])
        return ans


if __name__ == '__main__':
    nums = [4, 6, 7, 7]
    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]
    ans = Solution().findSubsequences(nums)
    print(ans)
