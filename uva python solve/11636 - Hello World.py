case = 1
while(1):
    n = int(input())
    if(n < 0):
        break
    if(n == 0 or n == 1):
        print('Case %d: 0' % case)
        case += 1
        continue

    c = 0
    t = 1
    while(1):
        d = t*2
        t = d
        c += 1
        if(t >= n):
            break
    print('Case %d: %d' % (case, c))
    case += 1
