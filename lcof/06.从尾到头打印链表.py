# -*- coding:utf-8 -*-
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head is None: return []
        if head.next is None: return [head.val]

        ans = []
        rev_head = self.reverseList(head)
        while rev_head:
            ans.append(rev_head.val)
            rev_head = rev_head.next
        return ans

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            next = head.next
            head.next = prev

            prev = head
            head = next
        return prev


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(3)
    l3 = ListNode(2)
    l1.next = l2
    l2.next = l3
    ans = Solution().reversePrint(l1)
    print(ans)
