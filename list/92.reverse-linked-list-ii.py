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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        global reverse_begin_pre
        if head is None: return None
        if m == n: return head

        temp = head

        count = 0
        reverse_begin_pre = None
        reverse_begin = None
        pre = None
        while head:
            count += 1

            # reverse m to n
            if m <= count < n or m < count <= n:
                if count == m:
                    reverse_begin_pre = pre
                    reverse_begin = head
                    pre = None

                if count == n:
                    next = head.next
                    head.next = pre
                    pre = head

                    if m == 1:
                        temp = head
                    else:
                        reverse_begin_pre.next = head
                    head = reverse_begin
                    head.next = next
                    continue

                next = head.next
                head.next = pre
                pre = head
                head = next
                continue

            pre = head
            head = head.next

        # printList(temp)
        return temp


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
    m, n = 2, 4
    printList(t1)
    ans = Solution().reverseBetween(t1, m, n)
    printList(ans)
