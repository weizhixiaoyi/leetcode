# -*- coding:utf-8 -*-

n = int(input().strip())
h = list(map(int, input().strip().split()))
m = int(input().strip())
w = list(map(int, input().strip().split()))

# n = 3
# h = [2, 2, 3]
# m = 2
# w = [3, 1]

h = sorted(h, reverse=True)
from collections import defaultdict

w_dict = defaultdict(int)
for ww in w:
    w_dict[ww] += 1
w_dict = sorted(w_dict.items(), key=lambda d: d[0])
w_dict = dict(w_dict)

count = 0
for stu_num in h:
    for w_key, w_value in w_dict.items():
        if w_key >= stu_num:
            count += 1
            if w_dict[w_key] == 1:
                w_dict.pop(w_key)
            else:
                w_dict[w_key] -= 1
            break

print(count)
