# -*- coding:utf-8 -*-


def solve(n, lines):
    lines_len = len(lines)
    for i in range(lines_len):
        print(lines[i])


if __name__ == '__main__':
    n = int(input())
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except:
            solve(n, lines)
            break
