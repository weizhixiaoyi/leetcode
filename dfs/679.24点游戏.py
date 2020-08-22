# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        target, epsilon = 24, 0.1

        def dfs(nums):
            if len(nums) == 1:
                # print(nums[0])
                if abs(nums[0] - target) < epsilon:
                    return True

            for i, a in enumerate(nums):
                for j, b in enumerate(nums):
                    if i == j:
                        continue
                    tmp = []
                    for k in range(len(nums)):
                        if k != i and k != j:
                            tmp.append(nums[k])

                    # a + b
                    tmp.append(a + b)
                    flag = dfs(tmp)
                    tmp.pop()
                    if flag: return True

                    # a - b
                    tmp.append(a - b)
                    flag = dfs(tmp)
                    tmp.pop()
                    if flag: return True

                    # b - a
                    tmp.append(b - a)
                    flag = dfs(tmp)
                    tmp.pop()
                    if flag: return True

                    # a * b
                    tmp.append(a * b)
                    flag = dfs(tmp)
                    tmp.pop()
                    if flag: return True

                    # a / b
                    if b != 0:
                        tmp.append(a / b)
                        flag = dfs(tmp)
                        tmp.pop()
                        if flag: return True

                    # b / a
                    if a != 0:
                        tmp.append(b / a)
                        flag = dfs(tmp)
                        tmp.pop()
                        if flag: return True

            return False

        ans = dfs(nums)
        return ans


if __name__ == '__main__':
    # nums = [4, 1, 8, 7]
    nums = [1, 2, 1, 2]
    ans = Solution().judgePoint24(nums)
    print(ans)
