# -*- coding:utf-8 -*-

class Solution:
    def solve(self, nums, nums_len):
        nums = sorted(nums, reverse=True)
        ans = 0
        for i in range(nums_len - 1):
            if nums[i] == -1: continue
            cur = nums[i]
            for j in range(i + 1, nums_len):
                if nums[j] == -1: continue
                if cur > nums[j]:
                    nums[i] = -1
                    nums[j] = -1
                    ans += 1
                    break
        # print(ans)
        # print(nums)
        for i in range(nums_len):
            if nums[i] == -1: continue
            ans += 1
        return ans


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    ans = Solution().solve(nums, n)
    print(ans)
