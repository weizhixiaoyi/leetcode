# -*- coding:utf-8 -*-
import sys

# input: t line
"""
t = int(input())
for i in range(t):
    value = input()
    print(value)
"""

# input: multi line
"""
for line in sys.stdin:
    print(line.strip())
    a = line.split()
    print(a)
"""

# input: multi line
"""
while True:
    try:
        a = input()
        # do something input
    except:
        break
"""

# use python class to realize struct
"""
class Item:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0


item = Item()
item.a = 1
item.b = 2
item.c = 3
"""

# Linked List
"""
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


node_a = Node(1)
node_b = Node(2)
node_c = Node(3)
node_a.next = node_b
node_b.next = node_c
"""

# dict sorted
"""
d = {
    'a': 1,
    'c': 3,
    'b': 2
}
kd = sorted(d.keys())
vd = sorted(d.values())
dd = sorted(d.items(), key=lambda d: d[0])
print(d)
print(kd)
print(vd)
print(dd)
"""

# 判断字符类别
"""
tr1 = 'abc'
str2 = '123'
str3 = '12a'
print(str1.isdigit()) # 判断是否为数字
print(str2.isalpha()) # 判断是否为字母
print(str3.isdecimal()) # 判断是否为字母或者数字的组合
for c in str1:
    print(c.isalpha())
"""

# list: if... else ...
"""
# for后面的if是筛选条件，不能够用else进行判断
a = [x for x in range(1, 10) if x % 2 == 0]
print(a)

# for前面是表达式, 必须根据x计算出结果
b = [x if x % 2 == 0 else None for x in range(1, 10)]
print(b)

# 总结而言：for前面是表达式, 必须带if else。 for后面是筛选条件，只能带if。
"""

# 求解二维数组最大值
"""
value = [[0, 0, 0, 1], [1, 1, 0, 1], [1, 2, 1, 1], [0, 1, 2, 2], [0, 1, 2, 3]]
max_value = max(map(max, value))
print(max_value)
"""

# copy and deepcopy
# 浅拷贝：创建一个新的组合对象，这个新对象与原对象共享内存中的子对象。
# 深拷贝：创建一个新的组合对象，同时递归地拷贝所有子对象，新的组合对象与原对象没有任何关联。
# 虽然实际上会共享不可变的子对象，但不影响它们的相互独立性。

"""
import copy

l = [1, 2, [3, 4]]
l1 = copy.copy(l)
l2 = copy.deepcopy(l)

l1.append(5)
print(l, l1, l2)
# [1, 2, [3, 4]] [1, 2, [3, 4], 5] [1, 2, [3, 4]]

l1[2][0] = "#"
print(l, l1, l2)
# [1, 2, ['#', 4] [1, 2, ['#', 4], 5] [1, 2, [3, 4]]
"""
