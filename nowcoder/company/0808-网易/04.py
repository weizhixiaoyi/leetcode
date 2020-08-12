# -*- coding:utf-8 -*-

def solve(n, relation):
    return n


if __name__ == '__main__':
    nm = list(map(int, input().split()))
    n, m = nm[0], nm[1]
    relation = []
    for t in range(m):
        cur = list(map(int, input().split()))
        relation.append(cur)
    ans = solve(n, relation)
    print(ans)
