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
    """
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None: return head

        # 哨兵节点
        begin = ListNode(-1)
        begin.next = head
        temp = begin

        while head:
            # 奇数个节点中, 最后一个节点不需要交换
            if head.next is None:
                head = head.next
                continue

            if head.next.next:
                # 旋转前设置begin, first, second, end
                first = head
                second = head.next
                end = head.next.next

                # 旋转
                second.next = first
                begin.next = second
                first.next = end

                # 旋转后归位
                head = end
                begin = first
            else:
                first = head
                second = head.next

                begin.next = second
                second.next = first

                first.next = None
                head = None

            # printList(temp)

        # printList(temp.next)
        return temp.next
    """

    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        cur = dummy
        while cur.next and cur.next.next:
            start, end = cur.next, cur.next.next
            cur.next = end
            start.next = end.next
            end.next = start

            cur = start

        return dummy.next


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
    printList(t1)
    ans = Solution().swapPairs(t1)
    printList(ans)
