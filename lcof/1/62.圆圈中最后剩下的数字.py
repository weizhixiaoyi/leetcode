# -*- coding:utf-8 -*-

class Solution:
    # def lastRemaining(self, n: int, m: int) -> int:
    #     nums, nums_len = [i for i in range(n)], n
    #     if nums_len == 1: return 0
    #
    #     idx = 0
    #     m -= 1
    #     while nums_len != 1:
    #         idx = (idx + m) % nums_len
    #         nums.remove(nums[idx])
    #         nums_len -= 1
    #
    #     return nums[0]

    def lastRemaining(self, n: int, m: int) -> int:
        pos = 0
        for i in range(2, n + 1):
            pos = (pos + m) % i
        return pos


if __name__ == '__main__':
    n, m = 10, 17
    ans = Solution().lastRemaining(n, m)
    print(ans)
