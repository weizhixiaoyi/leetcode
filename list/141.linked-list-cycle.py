# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None: return False
        if head.next is None: return False

        first = head
        second = head
        while first and second and second.next:
            first = first.next
            second = second.next.next
            if first == second:
                return True

        return False


if __name__ == '__main__':
    t0 = ListNode(1)
    t1 = ListNode(3)
    t2 = ListNode(2)
    t3 = ListNode(0)
    t4 = ListNode(-4)
    t0.next = t1
    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t2
    ans = Solution().hasCycle(t0)
    print(ans)
