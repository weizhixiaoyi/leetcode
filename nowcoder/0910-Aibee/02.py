# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None


def printList(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


def solve(nums, k):
    if not nums: return None
    nums_len = len(nums)
    if k >= nums_len: return nums

    tmp = ListNode()
    head = tmp
    for i in range(nums_len):
        cur = ListNode(nums[i])
        tmp.next = cur
        tmp = tmp.next
    # printList(head.next)

    # k reverse
    ans = head
    printList(ans.next)

    left1 = head
    left2 = head.next
    head = head.next
    cur_k = 0
    while head:
        cur_k += 1

        next = head.next

        if cur_k == k:
            right = head.next

            head.next = left1
            left2.next = right

            left1 = head
            left2 = right
            printList(head)

        head = head.next
    printList(ans.next)


if __name__ == '__main__':
    # nums = list(map(int, input().split()))
    # k = int(input())
    nums = [1, 2, 3, 4, 5]
    k = 2
    ans = solve(nums, k)
    print(ans)
