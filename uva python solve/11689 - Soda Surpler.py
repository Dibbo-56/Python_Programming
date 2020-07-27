t = int(input())
for i in range(0, t):
    e, f, c = map(int, input().split())
    d = e + f
    cnt = 0
    while(d >= c):
        cnt += int(d/c)
        left = d % c
        d = left + int(d/c)
    print(cnt)
