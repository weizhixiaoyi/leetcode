# -*- coding:utf-8 -*-

def solve(s, t):
    def rev(t):
        t_rev = ""
        for c in t:
            if c == "0":
                t_rev += "1"
            else:
                t_rev += "0"

        index = 0
        for c in t:
            if c == "0":
                index += 1
        t_rev = t_rev[index:]
        return t_rev

    s_rev = rev(s)
    t_rev = rev(t)
    if t == s: return True
    if t == s_rev: return True
    if t_rev == s: return True

    ss = s + s
    st = s + t
    st_rev = rev(st)
    if st_rev == ss: return True

    return False


if __name__ == '__main__':
    # t = 1
    t = int(input())
    for i in range(t):
        # s1 = "1100"
        # s2 = "110011"
        s1 = input()
        s2 = input()
        ans = solve(s1, s2)
        if ans:
            print("YES")
        else:
            print("NO")
