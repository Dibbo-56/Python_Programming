import math

t = int(input())
for i in range(0, t):
    x, y, r = map(int, input().split())
    sp = r - math.sqrt((x**2) + (y**2))
    lp = r + math.sqrt((x**2) + (y**2))
    print("%.2f %.2f" % (sp, lp))
