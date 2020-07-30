# -*- coding:utf-8 -*-

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_len, num2_len = len(num1), len(num2)
        i, j = num1_len - 1, num2_len - 1
        res, carry = '', 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i -= 1
            j -= 1
        return '1' + res if carry else res


if __name__ == '__main__':
    num1 = '1'
    num2 = '9'
    ans = Solution().addStrings(num1, num2)
    print(ans)

