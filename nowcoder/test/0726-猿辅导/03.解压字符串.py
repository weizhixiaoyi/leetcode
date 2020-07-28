# -*- coding:utf-8 -*-

n = int(input())


def solve(line):
    ans = ''
    line_len = len(line)

    i, j = 0, 0
    ans = ''
    stack = []
    while i < line_len:
        c = line[i]
        if c == '(':
            stack.append(len(ans))
            i += 1
        elif 'A' <= c <= 'Z':
            ans += c
            i += 1
        elif '0' <= c <= '9':
            j = i
            while i < line_len and '0' <= line[i] <= '9':
                i += 1
            ans += ans[-1] * (int(line[j:i]) - 1)
        elif c == ')':
            i += 1
            j = i
            while i < line_len and '0' <= line[i] <= '9':
                i += 1
            start = stack.pop()
            # print(ans[start:], int(line[j:i]))
            ans += ans[start:] * (int(line[j:i]) - 1)
    return ans


for i in range(n):
    line = input()
    ans = solve(line)
    print(ans)
