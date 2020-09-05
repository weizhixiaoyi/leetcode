# -*- coding:utf-8 -*-


from copy import copy
from copy import deepcopy

a = '123'
b = a
print(id(a), id(b))
c = copy(a)
d = deepcopy(a)
print(id(c), id(d))

print()
a_list = [1, 2, 3]
b_list = a_list
print(id(a_list), id(b_list))
c_list = copy(a_list)
d_list = deepcopy(a_list)
print(id(c_list), id(d_list))
print()

aa_list = [[1, 2, 3], 4, 5]
bb_list = aa_list
print(id(aa_list), id(bb_list))
cc_list = copy(aa_list)
dd_list = deepcopy(aa_list)
print(id(cc_list), id(dd_list))
