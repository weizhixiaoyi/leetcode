# -*- coding:utf-8 -*-


def solve(n, m, machines, tasks):
    machines = sorted(machines, key=lambda d: (d[0], d[1]), reverse=True)
    tasks = sorted(tasks, key=lambda d: (d[0], d[1]), reverse=True)
    # print(machines, tasks)
    used = []

    ans1, ans2 = 0, 0
    for task in tasks:
        task_time, task_level = task[0], task[1]
        # 尝试是否能够安排
        for k in range(len(machines)):
            if k in used:
                continue
            machine_time = machines[k]
            if machine_time >= task_time:
                ans1 += 1
                ans2 += (200 * task_time + 3 * task_level)
                used.append(k)
                break
    print(ans1, ans2)


if __name__ == '__main__':
    # n, m = 1, 2
    # machines = [[100, 3]]
    # tasks = [[100, 2], [100, 1]]
    n, m = map(int, input().split())
    machines = []
    for i in range(n):
        time, level = map(int, input().split())
        machines.append([time, level])
    tasks = []
    for i in range(m):
        time, level = map(int, input().split())
        tasks.append([time, level])
    solve(n, m, machines, tasks)
