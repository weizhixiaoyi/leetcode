# -*- coding:utf-8 -*-

def solve(s):
    s = s.strip().split()
    if not s: return ''
    flag = False
    for c in s:
        if c != "undo" and c != "redo":
            flag = True
    if flag is False: return ''

    s_len = len(s)
    stack1 = []
    stack2 = []
    no = 0
    for k in range(s_len):
        if s[k] != "undo" and s[k] != "redo":
            stack1.append(s[k])
            continue
        if s[k] == "undo":
            if stack1:
                val = stack1.pop()
                stack2.append(val)
            else:
                no += 1
            continue
        if s[k] == "redo":
            if no == 0:
                val = stack2.pop()
                stack1.append(val)
            else:
                no -= 1
    # print(stack1)
    return " ".join(stack1)


if __name__ == '__main__':
    s = input()
    # s = "hello undo redo world."
    # s = "hello1 undo undo redo redo world undo redo"
    # s = " undo undo redo"
    # s = "hello undo redo word undo redo"
    ans = solve(s)
    print(ans)
