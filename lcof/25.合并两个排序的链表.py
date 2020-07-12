# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        if l2 is None: return l1

        merge = ListNode(None)
        ans = merge
        while l1 and l2:
            if l1.val < l2.val:
                merge.next = ListNode(l1.val)
                merge = merge.next
                l1 = l1.next
            else:
                merge.next = ListNode(l2.val)
                merge = merge.next
                l2 = l2.next

        if l1:
            merge.next = l1
        if l2:
            merge.next = l2

        return ans.next


if __name__ == '__main__':
    l11 = ListNode(1)
    l12 = ListNode(2)
    l13 = ListNode(4)
    l11.next = l12
    l12.next = l13

    l21 = ListNode(1)
    l22 = ListNode(3)
    l23 = ListNode(4)
    l21.next = l22
    l22.next = l23

    printList(l11)
    printList(l21)
    ans = Solution().mergeTwoLists(l11, l21)
    printList(ans)
