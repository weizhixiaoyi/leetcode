# -*- coding:utf-8 -*-
from typing import List


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
    # 方法一: 依次合并两个链表
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]

        # 合并两个有序链表
        def helper(l1, l2):
            merge = ListNode(None)
            ans = merge
            while l1 and l2:
                if l1.val <= l2.val:
                    merge.next = l1
                    l1 = l1.next
                    merge = merge.next
                else:
                    merge.next = l2
                    l2 = l2.next
                    merge = merge.next
            if l1:
                merge.next = l1
            if l2:
                merge.next = l2
            return ans.next

        ans = helper(lists[0], lists[1])
        # printList(ans)
        for i in range(2, len(lists)):
            ans = helper(ans, lists[i])
            # printList(ans)
        return ans
    """

    # 采用最小堆
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        values = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(values, (lists[i].val, i))
                lists[i] = lists[i].next

        dummy = ListNode(None)
        ans = dummy
        while values:
            val, idx = heapq.heappop(values)
            dummy.next = ListNode(val)
            dummy = dummy.next

            if lists[idx]:
                heapq.heappush(values, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return ans.next


if __name__ == '__main__':
    l11 = ListNode(1)
    l12 = ListNode(4)
    l13 = ListNode(5)
    l11.next = l12
    l12.next = l13

    l21 = ListNode(1)
    l22 = ListNode(3)
    l23 = ListNode(4)
    l21.next = l22
    l22.next = l23

    l31 = ListNode(2)
    l32 = ListNode(6)
    l31.next = l32

    lists = [l11, l21, l31]
    ans = Solution().mergeKLists(lists)
    printList(ans)
