# -*- coding:utf-8 -*-

file_path = '03.txt'
f = open(file_path)
lines = f.readlines()
lines = [line.strip().split() for line in lines]
n, m = int(lines[0][0]), int(lines[0][1])

c = lines[1: m + 1]
infos = lines[m + 1:]
print(c)
print(infos)

class_teacher_id = []
for cur_c in c:
    class_teacher_id.append(cur_c[1])
class_student_ids = []
for cur_c in c:
    class_student_ids.append(cur_c[3:])
print(class_teacher_id)
print(class_student_ids)

class_teacher_time = {teacher_id: [] for teacher_id in class_teacher_id}
class_student_time = {teacher_id: [] for teacher_id in class_teacher_id}
class_teacher_id2_student_id = {teacher_id: class_student_id for teacher_id, class_student_id in
                                zip(class_teacher_id, class_student_ids)}
print(class_teacher_id2_student_id)

for info in infos:
    id = info[1]
    time = info[2]
    if id in class_teacher_id:
        class_teacher_time[id].append(time)

print('#' * 10 + 'Teach In Out Time' + '#' * 10)
for key, value in class_teacher_time.items():
    value1 = [v for i, v in enumerate(value) if i % 2 == 0]
    value2 = [v for i, v in enumerate(value) if i % 2 == 1]
    class_teacher_time[key] = [value1, value2]
print(class_teacher_time)
