# -*- coding:utf-8 -*-

readme_file_path = 'README_old.md'
lines = open(readme_file_path, 'r').readlines()
lines = [line for line in lines if len(line) > 5]
lines = [line.strip('\n').replace(' ', '').split(',') for line in lines]
lines.sort(key = lambda d: d[1])
lines = [line[1:] for line in lines]
for line in lines:
    print(line)

new_file_path = 'README.md'
with open(new_file_path, 'w') as f:
    for line in lines:
        val = ', '.join(line)
        f.write(val + '  \n')
