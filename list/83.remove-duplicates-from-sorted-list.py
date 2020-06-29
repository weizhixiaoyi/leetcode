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
        value = set()
        pre = None
        temp = head
        while temp:
            next = temp.next

            # 如果该元素存在过则进行删除
            if temp.val in value:
                if temp.next:
                    pre.next = next
                    temp = next
                else:
                    pre.next = None
                    temp = next
                continue

            value.add(temp.val)
            pre = temp
            temp = temp.next

        # printList(head)
        return head


if __name__ == '__main__':
    t1 = ListNode(1)
    # t2 = ListNode(2)
    # t3 = ListNode(2)
    # t4 = ListNode(3)
    # t5 = ListNode(3)
    # t1.next = t2
    # t2.next = t3
    # t3.next = t4
    # t4.next = t5
    printList(t1)
    ans = Solution().deleteDuplicates(t1)
    printList(ans)
