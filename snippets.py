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
