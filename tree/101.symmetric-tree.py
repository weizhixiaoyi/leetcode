# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     def helper(root1, root2):
    #         if (root1 is None) and (root2 is None):
    #             return True
    #         if (root1 and root2 is None) or (root1 is None and root2):
    #             return False
    #         if (root1.val != root2.val):
    #             return False
    #
    #         if not helper(root1.left, root2.right):
    #             return False
    #
    #         if not helper(root1.right, root2.left):
    #             return False
    #         return True
    #
    #     ans = helper(root, root)
    #     return ans

    def isSymmetric(self, root: TreeNode) -> bool:
        from queue import Queue
        q1, q2 = Queue(), Queue()
        q1.put(root)
        q2.put(root)

        while not q1.empty() and not q2.empty():
            n1, n2 = q1.get(), q2.get()
            # print(n1.val, n2.val)
            # print(q1.empty(), q2.empty())
            if n1 and n2:
                if n1.val != n2.val:
                    return False
            if (n1 and not n2) or (not n1 and n2):
                return False

            if n1 and n2:
                q1.put(n1.left)
                q1.put(n1.right)
                q2.put(n2.right)
                q2.put(n2.left)

        return True


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(2)
    t4 = TreeNode(3)
    t5 = TreeNode(4)
    t6 = TreeNode(4)
    t7 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    ans = Solution().isSymmetric(t1)
    print('ans: ', ans)
