# -*- coding:utf-8 -*-
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None: return None

        self.head = None
        self.pre = None

        # 利用中序遍历
        # 想要指向前一个节点, 需要pre来保存上一个节点
        def helper(root):
            if root is None: return None

            helper(root.left)
            # solve
            if self.pre:
                # root的左节点指向前驱, pre的右节点指向后驱
                root.left = self.pre
                self.pre.right = root
            else:
                # 走到最小值head位置
                self.head = root
            # 记录上一个位置
            self.pre = root

            helper(root.right)

        helper(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head


if __name__ == '__main__':
    t1 = Node(4)
    t2 = Node(2)
    t3 = Node(5)
    t4 = Node(1)
    t5 = Node(3)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    ans = Solution().treeToDoublyList(t1)
    print(ans)
