t = int(input())
for i in range(0, t):
    a, b, c = map(int, input().split())
    if(a+b > c and b+c > a and c+a > b):
        if(a == b and b == c):
            print("Case %d: Equilateral" % (i+1))
        elif (a == b or b == c or c == a):
            print("Case %d: Isosceles" % (i+1))
        else:
            print("Case %d: Scalene" % (i+1))
    else:
        print("Case %d: Invalid" % (i+1))
