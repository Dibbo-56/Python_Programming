t = int(input())
for i in range(0, t):
    arr = list(map(int, input().split()))
    n = arr[0]
    idx = int(n/2) + 1
    print("Case %d: %d" % (i+1, arr[idx]))
