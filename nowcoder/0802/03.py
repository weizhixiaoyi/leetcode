# -*- coding:utf-8 -*-

# nmt = list(map(int, input().split()))
# n, m, t = nmt[0], nmt[1], nmt[2]
# nn, mm = [], []
# for i in range(n):
#     tmp = list(map(int, input().split()))
#     nn.append(tmp)
# for i in range(m):
#     tmp = list(map(int, input().split()))
#     mm.append(tmp)

n, m, t = 5, 1, 9
nn = [
    [9, 1],
    [4, 9],
    [3, 1],
    [2, 3],
    [6, 5]
]
mm = [
    [9, 8]
]
from collections import defaultdict

nn_dict = defaultdict(list)
for num_n in nn:
    nn_dict[num_n[1]].append(num_n[0])
nn_dict = dict(sorted(nn_dict.items(), key=lambda d: d[0], reverse=True))
for key, value in nn_dict.items():
    value = sorted(value)
    nn_dict[key] = value
nn_keys = nn_dict.keys()
nn_keys = sorted(nn_keys)

mm_dict = defaultdict(list)
for num_m in mm:
    mm_dict[num_m[1]].append(num_m[1])
mm_dict = dict(sorted(nn_dict.items(), key=lambda d: d[0], reverse=True))
for key, value in mm_dict.items():
    value = sorted(value)
    mm_dict[key] = value
mm_keys = mm_dict.keys()
mm_keys = sorted(mm_keys)
mm_keys_len = len(mm_keys)

# 只选择中餐
flag1 = False
min_value1 = float('inf')
for key, value in nn_dict.items():
    if key >= t:
        flag1 = True
        min_value1 = min(min_value1, value[0])
# 只选择晚餐
flag2 = False
min_value2 = float('inf')
for key, value in mm_dict.items():
    if key >= t:
        flag2 = True
        min_value2 = min(min_value2, value[0])

min_value3 = float('inf')
for key1, value1 in nn_dict.items():
    if key1 < t:
        need = t - key1
        for key2, value2 in mm_dict.items():
            if key2 >= need:
                min_value3 = min(min_value3, value1[0] + value2[0])

# 怎么选择都不够
max_n, max_m = 0, 0
for num_n in nn:
    max_n = max(max_n, num_n[1])
for num_m in mm:
    max_m = max(max_m, num_m[1])
max_t = max_n + max_m
# 只选择中餐或者晚餐

if t == 0:
    print(0)
elif max_t < t:
    print(-1)
elif flag1 or flag2:
    print(min(min_value1, min_value2, min_value3))
else:
    print(min_value3)

# 选择中餐和晚餐中最大
# def binary_search(nums, need):
#     left, right = 0, mm_keys_len - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] < need:
#             left += 1
#         if nums[mid] > need:
#             right -= 1
#
#     return nums[left]
