t = int(input())
for i in range(0, t):
    s, d = map(int, input().split())
    if(s < d or (s-d) % 2 != 0):
        print("impossible")
    else:
        a = (s+d) / 2
        b = a-d
        print("%d %d" % (a, b))
