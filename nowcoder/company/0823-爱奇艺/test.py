# -*- coding:utf-8 -*-

a = '123456678'
b = '456'
print(a.split(b))

while True:
    flag = False
    for i in range(len(ans)):
        for j in range(b_list_len):
            if b_list[j] in ans[i]:
                # 分成三段
                idx = ans[i].index(b_list[j])
                first = ans[i][0:idx]
                second = ans[i][idx: idx + len(b_list[j])]
                third = ans[i][idx + len(b_list[j]):]
                ans.remove(ans[i])
                ans.append(first)
                ans.append(second)
                ans.append(third)
    if flag:
        break
