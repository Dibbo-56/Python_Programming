t = int(input())
for i in range(0, t):
    L, W, H = map(int, input().split())
    if(L <= 20 and W <= 20 and H <= 20):
        print("Case %d: good" % (i+1))
    else:
        print("Case %d: bad" % (i+1))
