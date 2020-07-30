# -*- coding:utf-8 -*-

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        num1_len, num2_len = len(num1), len(num2)
        multi = []
        for j in range(num2_len - 1, -1, -1):
            cur_multi = '0' * (num2_len - j - 1)
            carry = 0

            n2 = int(num2[j])
            for i in range(num1_len - 1, -1, -1):
                n1 = int(num1[i])
                tmp = n1 * n2 + carry
                carry = tmp // 10
                cur_multi = str(tmp % 10) + cur_multi
            if carry: cur_multi = str(carry) + cur_multi
            multi.append(cur_multi)

        ans = ''
        for m in multi:
            ans = self.addStrings(ans, m)
        return ans

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
    num1 = '123'
    num2 = '456'
    print(int(num1) * int(num2))
    ans = Solution().multiply(num1, num2)
    print(ans)
