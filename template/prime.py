# -*- coding:utf-8 -*-


class Solution:
    def get_prime(self):
        n = 1000
        isPrime = [True for i in range(n + 1)]
        for i in range(2, int(n ** 0.5)):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False

        prime = [i for i in range(2, n) if isPrime[i] is True]
        print(prime)


if __name__ == '__main__':
    Solution().get_prime()
