# -*- coding:utf-8 -*-

class Solution:
    def get_prime(self):
        nums = 1000
        nums_sqrt = int(nums ** 0.5)
        isPrime = [True for i in range(0, nums)]
        for i in range(2, nums_sqrt):
            if isPrime[i]:
                for j in range(i*i, nums, i):
                    isPrime[j] = False

        prime = [i for i in range(2, nums) if isPrime[i] == True]
        print(prime)

if __name__ == '__main__':
    Solution().get_prime()




