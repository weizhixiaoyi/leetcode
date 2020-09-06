# -*- coding:utf-8 -*-

n = 3
nums = [
    [2, 0],
    [1, 2],
    [-1, 2]
]
for num in nums:
    if num[1] == 0:
        continue
    else:
        num[1] -= 2
matrix = [[0 for j in range(n)] for i in range(n)]
for i, num in enumerate(nums):
    cur, pre = i, num[1]
    matrix[pre][cur] = 1
print(matrix)
