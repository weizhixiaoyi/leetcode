# -*- coding:utf-8 -*-


class Solution:
    def solve(self, n, nums):
        left, right = -10.00, 10.00
        ans = 0
        min_value = float('inf')
        while left <= right:
            left += 0.01
            x_value = []
            for i in range(0, n + 1, 1):
                x_value.append(pow(left, i))
            each_value = []
            for i in range(0, n + 1, 1):
                each_value.append(x_value[i] * nums[n - i])
                # print(left, i, x_value[i], nums[n - i])
            cur_sum = sum(each_value)
            if min_value < cur_sum:
                ans = left
        ans = sorted(ans)
        ans = [format(v, '.2f') for v in ans]
        ans = list(set(ans))
        if not ans:
            print('No')
        else:
            print(' '.join(ans))
        # print(format(ans, '.2f'))


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    Solution().solve(n, nums)
