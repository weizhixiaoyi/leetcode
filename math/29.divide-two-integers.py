# -*- coding:utf-8 -*-

class Solution:
    def divide(self, dividend: int, divisor: int) -> None:
        max_value = pow(2, 31) - 1
        if dividend == 0: return 0
        if divisor == 1: return dividend
        if divisor == -1:
            if abs(dividend) > max_value:
                return max_value
            else:
                return -dividend

        flag = False
        if dividend < 0 and dividend < 0: dividend, divisor = -dividend, -divisor
        if dividend < 0 and divisor > 0:
            dividend = - dividend
            flag = True
        if dividend > 0 and divisor < 0:
            divisor = - divisor
            flag = True

        # 依次进行相减会超时, 采用递归的方法, 每次进行加半寻找解空间.
        def helper(a, b):
            # 截止条件
            if a < b: return 0

            count = 1
            value = b
            while value + value < a:
                count += count
                value += value

            # 递归依次处理
            return count + helper(a - value, b)

        ans = helper(dividend, divisor)
        if flag:
            return -ans
        else:
            return ans


if __name__ == '__main__':
    dividend = -214783648
    divisor = -2
    ans = Solution().divide(dividend, divisor)
    print('ans: ', ans)
