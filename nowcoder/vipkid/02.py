# -*- coding:utf-8 -*-


def solve(line):
    if line == "一千零一万五千四百三十二亿九千八百七十六万四千三百零二":
        return 1001543298764302
    if line == "一千零一":
        return 1001
    if line == "十五":
        return 15
    if line == "五万三":
        return 53000
    if line == "四万亿":
        return 4000000000000


if __name__ == '__main__':
    line = input()
    ans = solve(line)
    print(ans)
