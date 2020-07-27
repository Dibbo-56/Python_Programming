case = 1
while True:
    n, l = map(int, input().split())
    if n == -1 and l == -1:
        break
    d = n
    c = 0
    while True:
        if d == 1:
            c += 1
            break
        elif d % 2 == 0:
            c += 1
            d = d / 2
        else:
            c += 1
            d = (3*d)+1
        if d > l:
            break
    print("Case %d: A = %d, limit = %d, number of terms = %d" %(case, n, l, c))
    case += 1
