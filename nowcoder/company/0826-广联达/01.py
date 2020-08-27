# -*- coding:utf-8 -*-


def solve(right, cur):
    right_len = len(right)
    # print(right)
    # print(cur)
    val = 0
    for i in range(right_len):
        if right[i] == cur[i]:
            val += 20
        else:
            if val < 10:
                continue
            else:
                val -= 10
    return val


if __name__ == '__main__':
    right = list(input())
    cur = list(input())
    ans = solve(right, cur)
    print(ans)
