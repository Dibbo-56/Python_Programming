t = 1
while(True):
    r, n = map(int, input().split())
    if(r == 0 and n == 0):
        break
    d = r-n
    for i in range(0, 27):
        R = n*i
        if(R >= d):
            print("Case %d: %d" % (t, i))
            break
    if (R < d):
        print("Case %d: impossible" % t)
    t += 1
