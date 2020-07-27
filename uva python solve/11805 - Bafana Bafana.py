t = int(input())

for i in range(t):
    l = list(map(int, input().split()))
    n, k, p = l[0], l[1], l[2]
    if (k+p == n):
        print('Case %d: %d' % (i+1, n))
    else:
        for j in range(p):
            if (k == n):
                k = 0
            k = k+1
        print("Case %d: %d" % (i+1, k))
