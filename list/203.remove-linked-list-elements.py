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
    # 头部节点不好处理, 可增加在头部增加哨兵节点, 将头部节点转变为中间节点
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None: return None
        temp = head
        pre = None
        while head:
            if head.val == val:
                if pre is None:
                    # 头部节点
                    temp = temp.next
                    head = head.next
                elif head.next:
                    # 中间节点
                    pre.next = head.next
                    head = head.next
                else:
                    # 尾部节点
                    pre.next = None
                    head = None  # 最后停止整体循环
                continue

            pre = head
            head = head.next

        return temp


if __name__ == '__main__':
    t1 = ListNode(6)
    t2 = ListNode(6)
    t3 = ListNode(2)
    t4 = ListNode(6)
    t5 = ListNode(4)
    t6 = ListNode(6)
    t7 = ListNode(6)
    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5
    t5.next = t6
    t6.next = t7
    val = 6
    printList(t1)
    ans = Solution().removeElements(t1, val)
    printList(ans)
