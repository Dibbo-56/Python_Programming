t = int(input())
for i in range(0, t):
    n, k, x = map(int, input().split())
    sum = (n * (n+1)) / 2
    l = x
    h = x + k
    for j in range(l, h):
        sum -= j
    print("Case %d: %d" % (i+1, sum))
