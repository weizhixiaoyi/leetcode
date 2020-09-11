# -*- coding:utf-8 -*-

class Solution:
    def solve(self, M, K, N, A, B):
        # print(M, K, N)
        # print(A)
        # print(B)

        # ans = [['0' for j in range(N)] for i in range(M)]
        B_dict = {}
        for j in range(N):
            col = []
            for i in range(K):
                col.append(B[i][j])
            B_dict[j] = col
        # print(B_dict)

        for i in range(M):
            line = A[i]
            for j in range(N):
                cur_value = 0
                for k in range(K):
                    cur_value += line[k] * B_dict[j][k]
                # for k in range(K):
                #     cur_value += line[k] * B[k][j]
                # ans[i][j] = str(cur_value)
                print(cur_value, end=' ')
            print()
        # print(ans)
        # for i in range(M):
        #     line = ' '.join(ans[i])
        #     print(line)


if __name__ == '__main__':
    mkn = list(map(int, input().strip().split()))
    M, K, N = mkn
    A = []
    for i in range(M):
        line = list(map(int, input().strip().split()))
        A.append(line)
    B = []
    for i in range(K):
        line = list(map(int, input().strip().split()))
        B.append(line)

    Solution().solve(M, K, N, A, B)

"""
2 2 2
1 2
3 4
1 2
3 4
"""
