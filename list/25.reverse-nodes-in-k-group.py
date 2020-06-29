# -*- coding:utf-8 -*-

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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None: return None

        pre = None
        cur_count = 0
        while head:
            if cur_count < k:
                next = head.next
                head.next = pre

                pre = head
                head = next

                cur_count += 1

            if cur_count == k:
                cur_count = 0
        printList(head)

    def reverse_list(self, head):
        if head is None or head.next is None: return head

        pre = None
        while head:
            next = head.next
            head.next = pre

            pre = head
            head = next

        return pre


if __name__ == '__main__':
    t1 = ListNode(1)
    t2 = ListNode(2)
    t3 = ListNode(3)
    t4 = ListNode(4)
    t5 = ListNode(5)
    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5
    k = 2
    printList(t1)
    ans = Solution().reverseKGroup(t1, k)
    printList(ans)
