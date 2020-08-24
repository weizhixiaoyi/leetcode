# -*- coding:utf-8 -*-


def solve(s):
    s_len = len(s)
    s_rev = s[::-1]
    if s_rev != s:
        return False
    s_could = ['A', 'H', 'I', 'M', 'O', 'T', 'V', 'W', 'X', 'Y']
    for i in range(s_len):
        if s[i] not in s_could:
            return False
    return True


if __name__ == '__main__':
    """
    while True:
        try:
            # s = "AHA"
            s = input().strip('\n')
            ans = solve(s)
            if ans:
                print("YES")
            else:
                print("NO")
        except:
            break
    """
    import sys
    for line in sys.stdin:
        line = line.strip()
        ans = solve(line)
        if ans:
            print("YES")
        else:
            print("NO")
