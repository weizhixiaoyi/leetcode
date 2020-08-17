# -*- coding:utf-8 -*-

import sys
from collections import defaultdict

file_dict = defaultdict(int)

if __name__ == '__main__':
    for line in sys.stdin:
        file_name_num = line.split('\\')[-1].strip('\n')
        file_dict[file_name_num] += 1
        print(file_dict)

    file_dict = dict(sorted(file_dict.items(), key=lambda d: d[1], reverse=True))
    count = 0
    for key, value in file_dict.items():
        if count > 7:
            break
        count += 1
        file_name, error_line = key.split(' ')
        if len(file_name) > 16:
            print(file_name[-16:], error_line, value)
        else:
            print(file_name, error_line, value)
