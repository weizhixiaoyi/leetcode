# -*- coding:utf-8 -*-


if __name__ == '__main__':
    t = int(input())
    for k in range(t):
        n, m = map(int, input().split())
        print('Case #' + str(k + 1) + ':')

        dir_l_dict = {
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
            (0, 1): (1, 0),
            (1, 0): (0, -1)
        }
        dir_r_dict = {
            (0, -1): (1, 0),
            (1, 0): (0, 1),
            (0, 1): (-1, 0),
            (-1, 0): (0, -1)
        }
        cur_x, cur_y = 0, 0
        dir_x, dir_y = 0, -1
        for i in range(m):
            line = input().split()
            op = line[0]
            if op == 'G':
                p = int(line[1])
                if dir_x == 1:
                    new_x = cur_x + p
                    cur_x = new_x if new_x < n else n - 1
                if dir_x == -1:
                    new_x = cur_x - p
                    cur_x = new_x if new_x >= 0 else 0
                if dir_y == 1:
                    new_y = cur_y + p
                    cur_y = new_y if new_y < n else n - 1
                if dir_y == -1:
                    new_y = cur_y - p
                    cur_y = new_y if new_y >= 0 else 0
            elif op == 'P':
                print(cur_x, cur_y)
            else:
                if op == 'L':
                    dir_x, dir_y = dir_l_dict[(dir_x, dir_y)]
                if op == 'R':
                    dir_x, dir_y = dir_r_dict[(dir_x, dir_y)]
