# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
    #     if A is None and B is None: return True
    #     if A is None or B is None: return False
    #
    #     from queue import Queue
    #     q = Queue()
    #     q.put(A)
    #
    #     while not q.empty():
    #         cur = q.get()
    #         if cur.val == B.val:
    #             if self.same(cur, B):
    #                 return True
    #
    #         if cur.left:
    #             q.put(cur.left)
    #         if cur.right:
    #             q.put(cur.right)
    #     return False

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A is None or B is None: return False

        # 如果找到一个相等的则进行返回
        if self.same(A, B):
            return True

        left = self.isSubStructure(A.left, B)
        right = self.isSubStructure(A.right, B)
        if left or right:
            return True
        return False

    def same(self, root1, root2):
        if root2 is None:
            return True
        # 放宽条件, 不需要完全相等, 但不能没有root1
        if root1 is None:
            return False
        if root1.val != root2.val:
            return False

        # 如果找到一个就返回, 确定返回条件
        if not self.same(root1.left, root2.left):
            return False
        if not self.same(root1.right, root2.right):
            return False

        return True


if __name__ == '__main__':
    t11 = TreeNode(3)
    t12 = TreeNode(4)
    t13 = TreeNode(5)
    t14 = TreeNode(1)
    t15 = TreeNode(2)
    t11.left = t12
    t11.right = t13
    t12.left = t14
    t12.right = t15

    t21 = TreeNode(4)
    t22 = TreeNode(1)
    t21.left = t22

    t31 = TreeNode(4)
    t32 = TreeNode(1)
    t31.left = t32

    ans = Solution().isSubStructure(t11, t21)
    print(ans)
    # print(Solution().same(t31, t21))
