# -*- coding:utf-8 -*-


def solve(a, b):
    square = [i * i for i in range(1, 501)]
    for i in range(1, 501):
        if i + a in square and i + b in square:
            return i


if __name__ == '__main__':
    line = input().split(',')
    a, b = int(line[0]), int(line[1])
    ans = solve(a, b)
    print(ans)
