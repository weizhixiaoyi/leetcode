# -*- coding:utf-8 -*-

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return None

        # 添加新节点 1->2->3; 1->1->2->2->3->3
        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = cur.next.next
        cur = head

        # 新节点增加random指针; 理解cur.next.random和cur.random.next意义
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        # 将链表拆分为二
        old_list = head
        new_list = head.next
        ans = new_list
        while old_list:
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next if new_list.next else None
            old_list = old_list.next
            new_list = new_list.next

        return ans


if __name__ == '__main__':
    n1 = Node(3)
    n2 = Node(3)
    n3 = Node(3)
    n1.next = n2
    n2.next = n3
    n1.random = n3.next
    n2.random = n1
    n3.random = n3.next
    ans = Solution().copyRandomList(n1)
