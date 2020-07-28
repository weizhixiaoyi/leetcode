# -*- coding:utf-8 -*-

# problem link: https://www.nowcoder.com/question/next?pid=22390442&qid=925105&tid=33906960
#
# 输入一个整形数值，返回一个整形值
# @param n int整型 n>9
# @return int整型
#
class Solution:
    def solution(self, n):
        # write code here
        ans = []
        while n != 1:
            for k in range(9, 0, -1):
                if k == 1:
                    return -1

                if n % k == 0:
                    ans.append(k)
                    n = n // k
                    break

        ans.reverse()
        fin = "".join([str(v) for v in ans])
        return int(fin)


if __name__ == '__main__':
    while True:
        n = int(input())
        s = Solution()
        ans = s.solution(n)
        print(ans)
