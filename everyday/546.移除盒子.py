# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        if not boxes: return 0
        nums = boxes

        self.ans = 0
        self.memo = {}

        def dfs(cur_nums):
            if not cur_nums: return 0
            if tuple(cur_nums) in self.memo:
                return self.memo[tuple(cur_nums)]

            ans = 0
            cur_nums_len = len(cur_nums)
            l, r = 0, 0
            while r < cur_nums_len:
                while r < cur_nums_len and cur_nums[r] == cur_nums[l]:
                    r += 1
                # print(cur_nums, l, r, cur_nums[l:r], (r - l) ** 2, cur_nums[:l] + cur_nums[r:])
                ans = max(ans, dfs(cur_nums[:l] + cur_nums[r:]) + (r - l) ** 2)
                # self.memo[tuple(cur_nums[:l] + cur_nums[r:])] = ans
                l = r
            self.memo[tuple(cur_nums)] = ans
            return ans

        return dfs(nums)


if __name__ == '__main__':
    # boxes = [1, 2, 2, 1]
    # boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
    # boxes = [1, 2, 3, 4, 1]
    boxes = [8, 1, 2, 10, 8, 5, 1, 10, 8, 4]
    ans = Solution().removeBoxes(boxes)
    print(ans)

    # test = [1, 2, 3, 4, 4, 4]
    # l, r = 0, 0
    # while r < len(test):
    #     while r < len(test) and test[r] == test[l]:
    #         r += 1
    #     print(l, r, test[l:r])
    #     print(test[:l] + test[r:])
    #     print(test)
    #     print()
    #     l = r
