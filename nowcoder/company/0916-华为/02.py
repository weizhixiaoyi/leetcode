# -*- coding:utf-8 -*-


class Solution:
    def solve(self, n):
        nums = [i + 1 for i in range(n)]
        # print(nums)
        nums_len = len(nums)

        left, cur_sum = 0, 0
        ans = []
        for i in range(nums_len):
            while cur_sum >= n:
                if cur_sum == n:
                    ans.append(nums[left: i])
                cur_sum -= nums[left]
                left += 1
            cur_sum += nums[i]
        return ans


if __name__ == '__main__':
    n = 15
    ans = Solution().solve(n)
    print(ans)
