# -*- coding:utf-8 -*-


def solve(line):
    line_len = len(line)

    for i in range(line_len - 1):
        for j in range(line_len - 1, i, -1):
            cur_str = line[i: j + 1]
            if isPar(cur_str):
                return cur_str


def isPar(cur_str):
    cur_str_len = len(cur_str)
    l, r = 0, cur_str_len - 1
    while l <= r:
        if cur_str[l] == cur_str[r]:
            l += 1
            r -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    line = input()
    ans = solve(line)
    print(ans)
