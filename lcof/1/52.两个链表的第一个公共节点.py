# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     if (headA is None) or (headB is None): return None
    #
    #     tempA = headA
    #     A_dict = {}
    #     while tempA:
    #         A_dict[id(tempA)] = tempA
    #         tempA = tempA.next
    #
    #     tempB = headB
    #     B_dict = {}
    #     while tempB:
    #         B_dict[id(tempB)] = tempB
    #         tempB = tempB.next
    #
    #     for key, value in A_dict.items():
    #         if key in B_dict:
    #             return value
    #
    #     return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1


if __name__ == '__main__':
    l11 = ListNode(0)
    l12 = ListNode(9)
    l13 = ListNode(1)

    l21 = ListNode(3)

    c1 = ListNode(2)
    c2 = ListNode(4)

    l11.next = l12
    l12.next = l13
    l13.next = c1
    c1.next = c2

    l21.next = c1
    c1.next = c2

    ans = Solution().getIntersectionNode(l11, l21)
    print(ans.val)
