# -*- coding:utf-8 -*-

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回能交换奖品的最大数量
# @param a int整型
# @param b int整型
# @param c int整型
# @return int整型
#
class Solution:
    def numberofprize(self, a, b, c):
        # write code here
        nums = [a, b, c]
        min_value = min(nums)
        for i in range(3):
            nums[i] -= min_value
        if sum(nums) == 0:
            return min_value

        ans = min_value
        nums = [val for val in nums if val != 0]
        nums = sorted(nums)
        # print(nums)

        if len(nums) == 2:
            if nums[0] % 2 == 0:
                half = nums[0] // 2
                ans += half
                nums = [nums[1] - 2 * half]
            else:
                half = nums[0] // 2
                ans += half
                nums = [1, nums[1] - 2 * half]
                if nums[1] >= 3:
                    ans += 1
                    nums = [nums[1] - 3]
                else:
                    return ans
        if len(nums) == 1:
            ans += (nums[0] // 5)
            return ans


if __name__ == '__main__':
    line = input().split(',')
    nums = map(int, line)
    a, b, c = nums
    ans = Solution().numberofprize(a, b, c)
    print(ans)
