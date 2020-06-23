# -*- coding:utf-8 -*-

class Solution:
    # 判断数是否已经存过, 如果存过则已陷入循环
    def isHappy(self, n: int) -> bool:
        cur_val = n
        all_digits = []
        while True:
            digits = self.get_digits(cur_val)
            # print(digits)
            digits_sum = sum([digit ** 2 for digit in digits])
            # print(digits_sum)
            if digits_sum == 1:
                return True
            if digits in all_digits:
                return False
            cur_val = digits_sum
            all_digits.append(digits)

    def get_digits(self, n):
        digits = []
        while n:
            digits.append(n % 10)
            n = n // 10
        return list(reversed(digits))


if __name__ == '__main__':
    n = 1222
    ans = Solution().isHappy(n)
    print('ans: ', ans)
