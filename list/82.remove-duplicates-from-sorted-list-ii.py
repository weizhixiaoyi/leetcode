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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None: return None
        pre = ListNode(-1000)
        pre.next = head
        temp = pre
        val = -999

        while head:
            # print(head.val, val)
            # printList(temp.next)
            if head.val == val:
                if head.next:
                    next = head.next
                    pre.next = next
                    head = next
                else:
                    pre.next = None
                    head = None
                # printList(temp.next)
                continue

            if head.next:
                # print(head.val, head.next.val)
                if head.val == head.next.val:
                    val = head.val

                    next = head.next
                    pre.next = next
                    head = next
                else:
                    pre = head
                    head = head.next
                # printList(temp.next)
            else:
                # printList(temp.next)
                # print(pre.val)
                # print(head.val)
                # pre.next = None
                head = None

        # printList(temp.next)
        return temp.next


if __name__ == '__main__':
    t0 = ListNode(1)
    t1 = ListNode(1)
    t2 = ListNode(2)
    t3 = ListNode(3)
    t4 = ListNode(3)
    t5 = ListNode(4)
    t6 = ListNode(4)
    t7 = ListNode(5)
    # t8 = ListNode(5)
    t0.next = t1
    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5
    t5.next = t6
    t6.next = t7
    # t7.next = t8
    printList(t0)
    ans = Solution().deleteDuplicates(t0)
    printList(ans)
