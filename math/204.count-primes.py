# -*- coding:utf-8 -*-

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        n_sqrt = int(n ** 0.5) + 1
        isPrime = [True for i in range(0, n)]
        for i in range(2, n_sqrt):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False

        prime = [i for i in range(2, n) if isPrime[i] == True]
        print(prime)
        return len(prime)


if __name__ == '__main__':
    n = 7
    ans = Solution().countPrimes(n)
    print('ans: ', ans)
