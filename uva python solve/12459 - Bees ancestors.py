while True:
    n = int(input())
    if n == 0:
        break
    b1, b2 = 1, 1
    for i in range(n):
        b = b1 + b2
        b1 = b2
        b2 = b
    print("%d" % b1)
