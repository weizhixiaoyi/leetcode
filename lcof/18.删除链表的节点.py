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
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head is None: return None
        dummy = ListNode(-1)
        dummy.next = head
        ans = dummy

        while dummy:
            if dummy.next is not None:
                if dummy.next.val == val:
                    if dummy.next.next:
                        dummy.next = dummy.next.next
                    else:
                        dummy.next = None

            dummy = dummy.next
        return ans.next


if __name__ == '__main__':
    t1 = ListNode(4)
    # t2 = ListNode(5)
    # t3 = ListNode(1)
    # t4 = ListNode(9)
    # t1.next = t2
    # t2.next = t3
    # t3.next = t4
    val = 4
    ans = Solution().deleteNode(t1, val)
    printList(ans)
