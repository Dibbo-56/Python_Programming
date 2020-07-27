t = int(input())
for i in range(0, t):
    a = int(input())
    b = int(input())
    sum = 0
    for j in range(a, b+1):
        if(j % 2):
            sum += j
    print("Case %d: %d" % (i+1, sum))
