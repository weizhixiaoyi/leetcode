# -*- coding:utf-8 -*-
import sys


def solve(line):
    line = line.strip()
    line = line.split(';')
    part1, part2, part3 = line

    # entity prop
    entity_prop_dict = {}
    part1 = part1.split(',')
    for p in part1:
        l1, l2 = p.split(':')
        entity_prop_dict[l2] = l1

    sent = part2 + 'O'
    part3 = part3 + ' O'
    sent_label = part3.split(' ')
    # print(entity_prop_dict)
    # print(sent)
    # print(sent_label)

    sent_split = []
    tmp = []

    label = ''
    for i, c in enumerate(sent):
        if tmp and sent_label[i] == 'O':
            sent_split.append((tmp, entity_prop_dict[label]))
            tmp = []
            label = ''
        else:
            label = sent_label[i - 1]
            tmp.append(c)
    # print(sent_split)

    ans = []
    for s in sent_split:
        l1, l2 = s
        l1 = ''.join(l1)
        ans.append(l2 + ':' + l1)

    ans = ','.join(ans)
    return ans


if __name__ == '__main__':
    for line in sys.stdin:
        ans = solve(line)
        print(ans)

    # line = "time:月,time:日,loc:小区,loc:超市;5月1号在新龙城或浩客见;月 月 日 日 O 小区 小区 小区 O 超市 超市 O"
    # ans = solve(line)
    # print(ans)
