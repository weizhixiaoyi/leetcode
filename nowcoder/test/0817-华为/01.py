# -*- coding:utf-8 -*-
import sys

score = []


def update(left, right):
    score[left] = right


def query(left, right):
    return max(score[left:right + 1])


if __name__ == '__main__':
    while True:
        try:
            nm = list(map(int, input().split()))
            n, m = nm[0], nm[1]
            tmp = list(map(int, input().split()))
            score = tmp

            for i in range(0, m):
                cur = input().split()
                flag, left, right = cur[0], int(cur[1]), int(cur[2])
                if flag == "U":
                    left -= 1
                    update(left, right)
                if flag == "Q":
                    left, right = left - 1, right - 1
                    if left > right:
                        left, right = right, left
                    cur_ans = query(left, right)
                    print(cur_ans)
        except:
            break
