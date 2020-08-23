# -*- coding:utf-8 -*-

def solve(line):
    if len(line) > 10:
        return False
    for c in line:
        if not c.isalpha():
            return False
    return True


if __name__ == '__main__':
    n = int(input())
    ans = 0
    for i in range(n):
        line = input()
        if solve(line):
            ans += 1

    print(ans)
