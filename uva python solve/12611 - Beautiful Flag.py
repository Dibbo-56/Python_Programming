t = int(input())
for i in range(0, t):
    r = int(input())
    l = (100*r) / 20
    x1 = (45*l) / 100
    x2 = (55*l) / 100
    y = (l*60) / 200
    print("Case %d:" % (i+1))
    print("-%d %d" % (x1, y))
    print("%d %d" % (x2, y))
    print("%d -%d" % (x2, y))
    print("-%d -%d" % (x1, y))
