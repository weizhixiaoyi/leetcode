# -*- coding:utf-8 -*-


# *解包过程
def solve(*args, **kwargs):
    for v in args:
        print(v)

    for k, v in kwargs.items():
        print(k, v)


# *args: position arguments
print('*args')
solve(1, 2, 3)

# **kwargs: key word argument
print('**kwargs')
solve(1, 2, 3, k1=1, k2=2)
