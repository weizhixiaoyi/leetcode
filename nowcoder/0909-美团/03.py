# -*- coding:utf-8 -*-


class Solution:
    def solve(self, nums, nums_len):
        if not nums: return 0

        ans = 0
        for i in range(nums_len):
            a = nums[i]
            for j in range(1, i + 2):
                a ^= ((i + 1) % j)
                # print(i + 1, j, (i + 1) % j, a)
            if (n - (i + 1)) % 2 != 0:
                a ^= ((i + 1) % n)

            if i == 0:
                ans = a
            else:
                ans ^= a

        return ans


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    # n = 10
    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ans = Solution().solve(nums, n)
    print(ans)
