# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None: return None
        if head.next is None: return None

        first = head
        second = head
        meet = None
        while first and second and second.next:
            first = first.next
            second = second.next.next
            if first == second:
                meet = first
                break
        if meet is None: return None

        begin = head
        while begin:
            if begin == first:
                return begin
            begin = begin.next
            first = first.next

if __name__ == '__main__':
    t1 = ListNode(3)
    t2 = ListNode(2)
    t3 = ListNode(0)
    t4 = ListNode(-4)
    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t2
    ans = Solution().detectCycle(t1)
    print(ans)
