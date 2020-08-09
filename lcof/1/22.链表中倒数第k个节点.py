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
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head is None: return None
        list_len = 0
        dummy_head = head
        while dummy_head:
            list_len += 1
            dummy_head = dummy_head.next

        if k > list_len:
            return None

        cur_node = 0
        while head:
            if cur_node == (list_len - k):
                return head
            cur_node += 1
            head = head.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    k = 2
    ans = Solution().getKthFromEnd(l1, k)
    printList(ans)
