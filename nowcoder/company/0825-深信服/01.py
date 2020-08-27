# -*- coding:utf-8 -*-


def solve(n):
    if n < 4: return 0
    if n == 4: return 1

    ans = 0
    while n > 3:
        cur_max = 0
        cur_need = 0
        for i in range(10001, 0, -1):
            for j in range(10001, 0, -1):
                need = 2 * i * j + i + j
                if need <= n and i * j > cur_max:
                    cur_max = i * j
                    cur_need = need
        n -= cur_need
        ans += cur_max
    return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        ans = solve(n)
        print(ans)

"""
作者：Lemon🌈201910231904756
链接：https://www.nowcoder.com/discuss/488631?type=all&order=time&pos=&page=1&channel=1013&source_id=search_all
来源：牛客网

t=int(input())
for _ in range(t):
    x = int(input())
    if x<4:
        print(0)
    else:
        i=1
        while x>=(i+1)*2*i:
            i+=1
        x -= i * 2 * (i - 1)
        ans=(i-1)**2
        while x>=3:
            x-=3
            ans+=1
            if x>2*(i-1):
                x-=2*(i-1)
                ans+=i-1
            else:
                ans+=x//2
                break
            i+=1
        print(ans)
"""
