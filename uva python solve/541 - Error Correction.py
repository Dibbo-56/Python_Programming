while True:
    n = int(input())
    if n==0:
        break

    a = []
    for i in range(n):
        l = list(map(int,input().split()))
        a.append(l)

    r,c = 0,0
    for i in range(n):
        sr = 0
        for j in range(n):
            sr += a[i][j]
        if sr%2!=0:
            r += 1
            k = i

    for j in range(n):
        sc = 0
        for i in range(n):
            sc += a[i][j]
        if sc%2!=0:
            c += 1
            l = j

    if r==0 and c==0:
        print("OK")
    elif r==1 and c==1:
        print("Change bit (%d,%d)" %(k+1,l+1))
    else:
        print("Corrupt")
