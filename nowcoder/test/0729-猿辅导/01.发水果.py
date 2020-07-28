# -*- coding:utf-8 -*-

nm = list(map(int, input().split()))
n, m = nm[0], nm[1]
nums = []
for i in range(n):
    line = list(map(int, input().split()))
    nums.append(line)

# n, m = 3, 3
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

left, right = 0, m - 1
head, tail = 0, n - 1

ans = []
while True:
    # head to tail
    for k in range(head, tail + 1):
        ans.append(nums[k][left])
    left += 1
    if left > right: break

    # left to right
    for k in range(left, right + 1):
        ans.append(nums[tail][k])
    tail -= 1
    if head > tail: break

    # tail to head
    for k in range(tail, head - 1, -1):
        ans.append(nums[k][right])
    right -= 1
    if left > right: break

    # right to left
    for k in range(right, left - 1, -1):
        ans.append(nums[head][k])
    head += 1
    if head > tail: break

ans = list(map(str, ans))
ans = ' '.join(ans)
print(ans)
