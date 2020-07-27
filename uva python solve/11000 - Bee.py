while True:
    n = int(input())
    if n == -1:
        break
    b1, b2, sum = 1, 1, 0
    for i in range(n+1):
        b = b1+b2
        b1 = b2
        b2 = b
        sum += b1
    print("%d %d" % (b1-1, sum - b1+1))
