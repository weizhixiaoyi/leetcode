# -*- coding:utf-8 -*-

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
    def reverse_head_tail(self, head):
        pre = None
        while head != None:
            next = head.next
            head.next = pre

            pre = head
            head = next
        return pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        pre, end = dummy, dummy
        while end.next:
            for i in range(k):
                if end:
                    end = end.next
            if not end: break

            start, next = pre.next, end.next

            end.next = None
            pre.next = self.reverse_head_tail(start)
            start.next = next

            pre = start
            end = start

        return dummy.next


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
    k = 3
    ans = Solution().reverseKGroup(l1, k)
    printList(ans)
