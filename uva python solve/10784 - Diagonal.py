import math
case = 1
while(1):
    n = int(input())
    if(n == 0):
        break
    d = math.ceil((3 + math.sqrt(9 + 8*n)) / 2)
    print('Case %d: %d' % (case, d))
    case += 1
