# -*- coding:utf-8 -*-
import pprint

"""
当的时候，此时没必要进行改变字符，所以dp[i][j] = dp[i - 1][j - 1]
当word[i] != word[j]时候，则分情况进行讨论
①替换操作:可能word1的0~i-1位置与word2的0~j-1位置的字符都相同,
          只是当前位置的字符不匹配,进行替换操作后两者变得相同,
          所以此时dp[i][j]=dp[i-1][j-1]+1(这个加1代表执行替换操作)
②删除操作:若此时word1的0~i-1位置与word2的0~j位置已经匹配了,
          此时多出了word1的i位置字符,应把它删除掉,才能使此时word1的0~i(这个i是执行了删除操作后新的i)
          和word2的0~j位置匹配,因此此时dp[i][j]=dp[i-1][j]+1(这个加1代表执行删除操作)
③插入操作:若此时word1的0~i位置只是和word2的0~j-1位置匹配,
          此时只需要在原来的i位置后面插入一个和word2的j位置相同的字符使得
          此时的word1的0~i(这个i是执行了插入操作后新的i)和word2的0~j匹配得上,
          所以此时dp[i][j]=dp[i][j-1]+1(这个加1代表执行插入操作)
④由于题目所要求的是要最少的操作数:所以当word1[i] != word2[j] 时,
          需要在这三个操作中选取一个最小的值赋格当前的dp[i][j]
(三)总结:状态方程为:
if(word1[i] == word2[j]):
    dp[i][j] = dp[i-1][j-1]
else:
    min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0: return len(word2)
        if len(word2) == 0: return len(word1)

        # 初始化当某个字符串为空时所需花费的操作
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1): dp[i][0] = i
        for j in range(1, n + 1): dp[0][j] = j
        # pprint.pprint(dp)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[m][n]


# 自下而上的递归实现
class Solution1:
    import functools
    # functools是将计算结果缓存，节省内存，记住python递归时利用此函数
    @functools.lru_cache(None)
    def minDistance(self, word1: str, word2: str) -> int:
        # 递归的停止条件而不是最终的返回结果，比如肯定不是返回len(word1) + len(word2)，而是
        # 将此值返回给下面调用的位置self.minDistance(x, y)
        if len(word1) == 0 or len(word2) == 0:
            print("1: ", len(word1) + len(word2))
            return len(word1) + len(word2)

        if word1[-1] == word2[-1]:
            return self.minDistance(word1[:-1], word2[:-1])
        else:
            insert = self.minDistance(word1, word2[:-1]) + 1
            delete = self.minDistance(word1[:-1], word2) + 1
            replace = self.minDistance(word1[:-1], word2[:-1]) + 1
            print("2: ", min(insert, delete, replace))
            return min(insert, delete, replace)


if __name__ == '__main__':
    word1, word2 = "horse", "ros"
    solution = Solution1()
    ans = solution.minDistance(word1, word2)
    print('ans: ', ans)
