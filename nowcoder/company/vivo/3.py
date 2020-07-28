# -*- coding:utf-8 -*-

"""
多链表合并，题目的场景设置是流水线合并。输入是行数和多行的数字。要将他们合并，返回一个链表。
例如
3
3 4 5 6
5 6 7 10
2 4
合并结果是
2 3 4 4 5 5 6 6 7 10
"""


class LinkList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


def merge(nums):
    linklists = []
    for num in nums:
        first = LinkList(num[0])
        cur = first
        for v in range(1, len(num)):
            temp = LinkList(num[v])
            cur.next = temp
            cur = cur.next
        linklists.append(first)

    all_value = []
    for first in linklists:
        while first:
            all_value.append(first.val)
            first = first.next
    all_value.sort()
    return all_value


if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(0, n):
        temp = input().split()
        num = [int(v) for v in temp]
        nums.append(num)

    ans = merge(nums)
    for v in ans:
        print(v, end=" ")
