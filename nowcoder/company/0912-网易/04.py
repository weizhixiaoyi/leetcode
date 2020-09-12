# -*- coding:utf-8 -*-


class Solution:
    def solve(self, bidxs, gidxs, match, match_len):
        return min(len(bidxs), len(gidxs))


if __name__ == '__main__':
    bidxs = list(map(int, input().split()))
    gidxs = list(map(int, input().split()))
    n = int(input())
    match = []
    for i in range(n):
        b, g = map(int, input().split())
        match.append([b, g])
    ans = Solution().solve(bidxs, gidxs, match, n)
    print(ans)
