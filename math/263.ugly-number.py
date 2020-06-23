# -*- coding:utf-8 -*-

class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0: return False
        prime, prime_len = [2, 3, 5], 3
        while True:
            flag = False
            for i in range(prime_len):
                if num % prime[i] == 0:
                    # print(prime[i])
                    num = num // prime[i]
                    flag = True

            if num == 1 or num == -1:
                return True
            if flag == False:
                return False


if __name__ == '__main__':
    import math
    num = -2147483648
    ans = Solution().isUgly(num)
    print('ans: ', ans)
