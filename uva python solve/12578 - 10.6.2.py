import math

t = int(input())
for i in range(0, t):
    l = int(input())
    pi = math.pi
    w = float(6*l) / 10
    r = float(2*l) / 10
    c = pi*r*r
    g = (w*l) - c
    print("%.2f %.2f" % (c, g))
