# -*- coding:utf-8 -*-
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printList(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None: return None
        if head.next is None: return head

        prev = None
        while head:
            next = head.next
            head.next = prev

            prev = head
            head = next
        return prev


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    ans = Solution().reverseList(l1)
    printList(ans)
