# -*- coding:utf-8 -*-

class Solution:
    def getHouses(self, t, xa):
        t = float(t)
        nums = []
        xa_len = len(xa)
        for i in range(0, xa_len, 2):
            half = xa[i + 1] / 2
            left = xa[i] - half
            right = xa[i] + half
            nums.append([left, right])

        ans = 2
        nums_len = len(nums)
        for i in range(nums_len - 1):
            if nums[i + 1][0] - nums[i][1] > t:
                ans += 2
            if nums[i + 1][0] - nums[i][1] == t:
                ans += 1
        return ans


if __name__ == '__main__':
    t = 2
    xa = [-1, 4, 5, 2]
    ans = Solution().getHouses(t, xa)
    print(ans)
