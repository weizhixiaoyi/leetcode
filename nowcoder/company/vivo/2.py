# -*- coding:utf-8 -*-

"""
测试手机防摔功能。给两个数字，K,V。K表示有多少部手机，V表示楼层数目。返回测试出结果至少要的次数。
比如 K是1 V是2
如果在第一层 往下摔手机，如果摔坏了。抗摔能力就是0层
如果没摔坏，第二层摔手机，如果坏了，抗摔能力就是1层
如果没坏，抗摔能力就是2层。
所以要测试出结果，需要摔两次手机，程序返回 2
如果一开始在2层摔手机，并坏了，则无法得到结果。
"""
import math


def solution(k, n):
    ans = int(math.log(n))
    print(ans)
    print(math.log(2))
    return ans + 1


if __name__ == '__main__':
    temp = input().split(" ")
    print(temp)
    k, n = int(temp[0]), int(temp[1])
    ans = solution(k, n)
    print(ans)
