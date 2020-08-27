# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head: return None

        slow, fast = head, head
        cur_k = 0
        while fast:
            fast = fast.next
            cur_k += 1
            if cur_k > k:
                slow = slow.next
        return slow


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
    ans = Solution().getKthFromEnd(t1, k)
    print(ans.val)
