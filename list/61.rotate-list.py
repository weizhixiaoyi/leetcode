# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printList(l):
    while l:
        print(l.val, end=' ')
        l = l.next
    print()


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None: return None
        if head.next is None: return head
        if head.next.next is None:
            if k % 2 == 0:
                return head
            if k % 2 != 0:
                first = head
                second = head.next
                second.next = first
                first.next = None
                return second

        l_len = 0
        temp = head
        while temp:
            temp = temp.next
            l_len += 1
        k = k % l_len

        def helper(l):
            l_first = l

            while l:
                l = l.next
                if l.next and l.next.next is None:
                    l.next.next = l_first
                    first = l.next
                    l.next = None
                    break

            # printList(first)
            return first

        # helper(head)
        for i in range(0, k):
            head = helper(head)
        return head


if __name__ == '__main__':
    l1 = ListNode(0)
    l2 = ListNode(1)
    l3 = ListNode(2)
    # l4 = ListNode(4)
    # l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    # l3.next = l4
    # l4.next = l5
    k = 5
    printList(l1)
    ans = Solution().rotateRight(l1, k)
    printList(ans)
