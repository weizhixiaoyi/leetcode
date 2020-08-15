# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[0] == 0: return [1]

        digits_len = len(digits)
        i = digits_len - 1
        digits[i] += 1

        carry = 0
        while i >= 0:
            digits[i] = digits[i] + carry
            if digits[i] >= 10:
                carry = 1
                digits[i] = digits[i] % 10
            else:
                carry = 0
            i -= 1

        if carry:
            digits = [carry] + digits
        return digits


if __name__ == '__main__':
    digits = [8, 9, 9, 9]
    ans = Solution().plusOne(digits)
    print(ans)
